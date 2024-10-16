import cv2
import os
import base64
import openai
import time

from openai import OpenAI

# Add the client id here 
client = OpenAI(api_key="") 


def extract_frames(video_path, output_folder, frame_interval=60):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return []

    frame_count = 0
    extracted_frame_paths = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_filename = f"{output_folder}/frame_{frame_count}.jpg"
            cv2.imwrite(frame_filename, frame)
            extracted_frame_paths.append(frame_filename)

        frame_count += 1

    cap.release()
    print(f"Frame extraction complete. {len(extracted_frame_paths)} frames extracted.")

    return extracted_frame_paths

def get_video_duration(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return 0

    fps = cap.get(cv2.CAP_PROP_FPS)  # Get frame rate
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Get total frame count

    duration = round(frame_count / fps) if fps > 0 else 0  # Round the duration

    cap.release()
    return duration

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def get_frame_descriptions(frame_paths, final_prompt, max_retries=3, retry_delay=2):
    base64_frames = [image_to_base64(path) for path in frame_paths]

    prompt_messages = [
        {
            "role": "user",
            "content": [
                *map(lambda x: {"image": x, "resize": 768}, base64_frames),
                final_prompt
            ]
        }
    ]

    params = {
        "model": "gpt-4o-mini",
        "messages": prompt_messages,
        "max_tokens": 1000,
        "temperature": 0
    }

    for attempt in range(max_retries):
        try:
            result = client.chat.completions.create(**params)
            return result.choices[0].message.content
        except openai.InternalServerError as e:
            print(f"Server error on attempt {attempt + 1}: {e}. Retrying after {retry_delay} seconds...")
            time.sleep(retry_delay)

    print("Failed to obtain descriptions after several retries.")
    return None

# Main execution
# video_path = "video.mp4"
video_path = "v2.mp4"
output_folder = "extracted_frames"

# Calculate video duration and adjust prompt
video_duration = get_video_duration(video_path)
print(f"Video duration: {video_duration} seconds.")

word_count = video_duration * 2.5
print(f"Word Count: {word_count}")

prompt = f"(This video is ONLY {video_duration} seconds long, so make sure the voiceover MUST be less than {word_count} words)"

# final_prompt = "ACT as an commentator. In a conversational style, explain step-by-step what is happening in match the frames suitable for a voiceover." + prompt
final_prompt = "ACT as an commentator. In a conversational style, explain step-by-step what is happening in valorant game the frames suitable for a voiceover." + prompt

# Extract frames and get descriptions
extracted_frames = extract_frames(video_path, output_folder)
print("extracted_frames",extracted_frames)
descriptions = get_frame_descriptions(extracted_frames, final_prompt)

print(descriptions)


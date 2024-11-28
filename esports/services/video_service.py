import cv2
import os
import base64
import time
from pathlib import Path
import whisper
from moviepy.editor import VideoFileClip
from openai import OpenAI
from django.conf import settings
from django.core.files.storage import default_storage
import numpy as np


class VideoProcessingService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.output_folder = settings.EXTRACTED_FRAMES_DIR
        self.temp_dir = settings.TEMP_DIR

    def process_video(self, video_file, text_type="normal", game_type=None):
        """
        Main method to process video and generate descriptions
        """
        try:

            # Save uploaded file temporarily
            video_path = self._save_temp_file(video_file)
            print("Video path generated:", video_path)

            # Process video
            video_duration = self.get_video_duration(video_path)
            word_count = int(video_duration * 2.2)
            print(f"Video duration: {video_duration} seconds")

            # Extract frames
            extracted_frames = self.extract_frames(video_path)
            print(f"Extracted {len(extracted_frames)} frames")

            # Extract and transcribe audio
            audio_path = self._save_temp_audio(video_path)
            print("Extracted audio to:", audio_path)

            # Transcribe audio
            audio_transcription = self.transcribe_audio(audio_path)

            # Generate descriptions
            prompt = self._generate_prompt(
                video_duration, word_count, text_type, game_type)
            frame_descriptions = self.get_frame_descriptions(
                extracted_frames, prompt)
            print("Frame descriptions:", frame_descriptions)

            # Combine and rewrite description
            combined_text = self._combine_descriptions(
                frame_descriptions, audio_transcription)
            final_description = self.get_rewritten_description(
                combined_text, video_duration, word_count)

            # Cleanup
            # self._cleanup_temp_files(video_path, audio_path, extracted_frames)

            return {
                'status': 'success',
                'description': final_description,
                'duration': int(video_duration),
                'word_count': word_count
            }

        except Exception as e:
            print(f"Error in process_video: {str(e)}")
            raise Exception(f"Video processing failed: {str(e)}")

    def extract_frames(self, video_path, frame_interval=60):
        """Extract frames from video"""
        Path(self.output_folder).mkdir(parents=True, exist_ok=True)
        # Clear the output folder
        for file_name in os.listdir(self.output_folder):
            file_path = os.path.join(self.output_folder, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {str(e)}")

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise Exception("Could not open video file")

        frame_paths = []
        frame_count = 0

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                if frame_count % frame_interval == 0:
                    frame_path = os.path.join(
                        self.output_folder, f"frame_{frame_count}.jpg")
                    cv2.imwrite(frame_path, frame)
                    frame_paths.append(frame_path)

                frame_count += 1
        finally:
            cap.release()

        if not frame_paths:
            raise Exception("No frames were extracted from the video")

        return frame_paths

    def get_video_duration(self, video_path):
        """Get video duration in seconds"""
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise Exception("Could not open video")

        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = round(frame_count / fps) if fps > 0 else 0

        cap.release()
        return duration

    def get_frame_descriptions(self, frame_paths, final_prompt, max_retries=3, retry_delay=2):
        """Get descriptions for extracted frames"""
        base64_frames = [self._image_to_base64(path) for path in frame_paths]

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
                result = self.client.chat.completions.create(**params)
                return result.choices[0].message.content
            except Exception as e:
                print(f"Server error on attempt {
                      attempt + 1}: {e}. Retrying after {retry_delay} seconds...")
                time.sleep(retry_delay)
                if attempt == max_retries - 1:
                    raise

        return None

    def transcribe_audio(self, audio_path):
        """Transcribe audio using Whisper"""
        try:
            print("Transcribing audio...")
            model = whisper.load_model("base")
            result = model.transcribe(audio_path)
            print("Audio transcription completed")
            return result["text"]
        except Exception as e:
            print(f"Error in audio transcription: {str(e)}")
            raise

    def get_rewritten_description(self, text, duration, word_count):
        """Get rewritten description from OpenAI"""
        try:
            system_prompt = (
                f"Use the Video Description to describe what's happening in the video "
                f"and use the Audio Transcription to complement the analysis into a "
                f"spoken report. The video is {
                    duration} seconds long, so keep it under {word_count} words."
            )

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text}
                ],
                max_tokens=1000,
                temperature=0.7
            )

            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in get_rewritten_description: {str(e)}")
            raise

    def _generate_prompt(self, duration, word_count, text_type, game_type):
        """Generate appropriate prompt based on type"""
        base_prompt = (
            f"(This video is ONLY {duration} seconds long, "
            f"so make sure the voiceover MUST be less than {word_count} words)"
        )

        style = "engaging and enthusiastic" if text_type == "creative" else "conversational"
        game_specific = f"in {game_type} game" if game_type else "in the match"

        return (
            f"ACT as a commentator. In a {style} style, explain step-by-step "
            f"what is happening {
                game_specific} suitable for a voiceover. {base_prompt}"
        )

    def _save_temp_file(self, file):
        """Save uploaded file temporarily"""
        try:
            temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
            if os.path.exists(temp_dir):
                for file_name in os.listdir(temp_dir):
                    file_path = os.path.join(temp_dir, file_name)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                    except Exception as e:
                        print(f"Error deleting file {file_path}: {str(e)}")

            path = default_storage.save(os.path.join('temp', file.name), file)
            return default_storage.path(path)
        except Exception as e:
            print(f"Error saving temporary file: {str(e)}")
            raise

    def _save_temp_audio(self, video_path):
        """Extract and save audio from video"""
        try:
            audio_path = os.path.join(
                self.temp_dir, f"{os.path.splitext(os.path.basename(video_path))[0]}.mp3")
            video = VideoFileClip(video_path)
            video.audio.write_audiofile(audio_path)
            return audio_path
        except Exception as e:
            print(f"Error extracting audio: {str(e)}")
            raise

    @staticmethod
    def _image_to_base64(image_path):
        """Convert image to base64"""
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except Exception as e:
            print(f"Error converting image to base64: {str(e)}")
            raise

    def _combine_descriptions(self, frame_descriptions, audio_transcription):
        """Combine frame descriptions with audio transcription"""
        return f"Video Description:\n{frame_descriptions}\n\nAudio Transcription:\n{audio_transcription}"

    def _cleanup_temp_files(self, video_path, audio_path, frame_paths):
        """Clean up temporary files"""
        try:
            # Remove temporary files
            files_to_remove = [video_path, audio_path, *frame_paths]
            for file_path in files_to_remove:
                try:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Warning: Failed to remove {file_path}: {str(e)}")
        except Exception as e:
            print(f"Warning: Cleanup error: {str(e)}")

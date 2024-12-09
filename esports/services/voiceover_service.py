from pathlib import Path
from moviepy.editor import VideoFileClip, AudioFileClip
from django.conf import settings
from openai import OpenAI
import os
import logging

logger = logging.getLogger(__name__)


class VoiceoverService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.temp_dir = settings.TEMP_DIR
        self.downloads_dir = settings.DOWNLOADS_DIR

    def create_videos_with_voiceover(self, text_english: str, text_french: str) -> dict:
        """
        Create voiceovers and merge with video for both languages.

        Args:
            text_english (str): English text for voiceover
            text_french (str): French text for voiceover

        Returns:
            dict: Paths to generated videos or error message
        """
        try:
            video_path = os.path.join(self.temp_dir, 'video.mp4')
            if not os.path.exists(self.downloads_dir):
                os.makedirs(self.downloads_dir)

            if not os.path.exists(video_path):
                raise FileNotFoundError(
                    "Video file not found in temp directory")

            # Setup paths
            output_audio_path = os.path.join(self.temp_dir, 'voiceover.mp3')
            output_audio_path_french = os.path.join(
                self.temp_dir, 'voiceover_french.mp3')

            output_video_path = os.path.join(
                self.downloads_dir, 'generated_video_english.mp4')
            output_video_path_french = os.path.join(
                self.downloads_dir, 'generated_video_french.mp4')

            # Create voiceovers
            self._create_voiceover(
                text_english, output_audio_path, voice="echo")
            self._create_voiceover(
                text_french, output_audio_path_french, voice="alloy")

            # Merge audio with video
            self._merge_audio_video(
                video_path, output_audio_path, output_video_path)
            self._merge_audio_video(
                video_path, output_audio_path_french, output_video_path_french)

            # Clean up audio files
            self._cleanup_files(output_audio_path, output_audio_path_french)

            return {
                'success': True,
                'english_video': output_video_path,
                'french_video': output_video_path_french
            }

        except Exception as e:
            logger.error(f"Video generation error: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }

    def _create_voiceover(self, text: str, output_audio_path: str, model="tts-1", voice="echo"):
        """Create voiceover using OpenAI's text-to-speech"""
        try:
            response = self.client.audio.speech.create(
                model=model,
                voice=voice,
                input=text
            )
            response.stream_to_file(Path(output_audio_path))
        except Exception as e:
            logger.error(f"Voiceover creation error: {str(e)}")
            raise

    def _merge_audio_video(self, video_path: str, audio_path: str, output_video_path: str):
        """Merge audio with video"""
        try:
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)
            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(
                output_video_path, codec="libx264", audio_codec="aac")

            # Clean up clips
            video_clip.close()
            audio_clip.close()
            final_clip.close()

        except Exception as e:
            logger.error(f"Video merging error: {str(e)}")
            raise

    def _cleanup_files(self, *file_paths):
        """Clean up temporary files"""
        for file_path in file_paths:
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
            except Exception as e:
                logger.warning(f"Failed to remove {file_path}: {str(e)}")

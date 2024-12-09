import os
from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from esports.services.video_service import VideoProcessingService
import json
import logging
from esports.services.translation_service import TranslationService
from esports.services.voiceover_service import VoiceoverService
from django.http import HttpResponse, JsonResponse
import zipfile
from io import BytesIO
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        try:
            print("request", request)
            # Get form data
            uploaded_file = request.FILES.get('file_upload')
            textarea_value = request.POST.get('textarea_field')
            game_type = request.POST.get('game_type')
            temperature = request.POST.get('temperature')

            logger.info(f"Received upload request - File: {uploaded_file}, Type: {
                        textarea_value}, Game: {game_type}")

            # Validate inputs
            if not all([uploaded_file, textarea_value, game_type]):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Missing required fields. Please provide all required information.'
                }, status=400)

            # Validate file type (optional but recommended)
            allowed_types = ['video/mp4', 'video/mpeg', 'video/quicktime']
            if uploaded_file.content_type not in allowed_types:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid file type. Please upload a valid video file.'
                }, status=400)

            # Process video using the service
            service = VideoProcessingService()
            generated_text = service.process_video(
                video_file=uploaded_file,
                text_type=textarea_value,
                game_type=game_type,
                temperature=temperature
            )

            # Return success response
            return JsonResponse({
                'status': 'success',
                'generated_text': generated_text,
                'uploaded_file_name': uploaded_file.name,
                'textarea_value': textarea_value,
                'game_type': game_type,
            })

        except Exception as e:
            logger.error(f"Error processing video: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': f'Failed to process the video: {str(e)}'
            }, status=500)

    # GET request - render the form template
    return render(request, 'index.html')


@csrf_exempt
def generate_french(request):
    """View for handling translation requests"""
    translation_service = TranslationService()

    if request.method == 'POST':
        try:
            generated_text_data = request.POST.get('generated_text_data')
            logger.info(f"Received translation request for text length: {
                        len(generated_text_data) if generated_text_data else 0}")

            result = translation_service.translate_to_french(
                generated_text_data)

            if result['success']:
                return JsonResponse({
                    'status': 'success',
                    'generated_text': result['translated_text']
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': result['error']
                }, status=400)

        except Exception as e:
            logger.error(f"Error in generate_french view: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': 'An unexpected error occurred'
            }, status=500)

    return render(request, 'index.html')


@csrf_exempt
def generate_video(request):
    if request.method == 'POST':
        try:
            text_english = request.POST.get('english_data')
            text_french = request.POST.get('french_data')

            if not all([text_english, text_french]):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Missing required texts'
                })

            # Generate videos with voiceovers
            voiceover_service = VoiceoverService()
            result = voiceover_service.create_videos_with_voiceover(
                text_english, text_french)

            if result['success']:
                return JsonResponse({
                    'status': 'success',
                    'english_video': result['english_video'],
                    'french_video': result['french_video']
                })

            return JsonResponse({
                'status': 'error',
                'message': 'Failed to generate videos'
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })

    return JsonResponse({
        'status': 'error',
        'message': 'Method not allowed'
    })


@csrf_exempt
def serve_video(request):
    video_path = request.GET.get('path')
    if video_path and os.path.exists(video_path):
        return FileResponse(open(video_path, 'rb'), as_attachment=True,
                            filename=os.path.basename(video_path))
    return JsonResponse({'error': 'File not found'})

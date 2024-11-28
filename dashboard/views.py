from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from esports.services.video_service import VideoProcessingService
import json
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        try:
            # Get form data
            uploaded_file = request.FILES.get('file_upload')
            textarea_value = request.POST.get('textarea_field')
            game_type = request.POST.get('game_type')

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
                game_type=game_type
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


def generate_french(request):
    if request.method == 'POST':
        # Assuming file and other form data is captured (as explained earlier)
        generated_text_data = request.POST.get('generated_text_data')

        if generated_text_data:

            # Return success response with video URL
            return JsonResponse({
                'status': 'success',
                'generated_text': ''' Assumons que la génération de l'URL de la vidéo ou le téléchargement de la vidéo soit réussi Assumons que la génération de l'URL de la vidéo ou le téléchargement de la vidéo soit réussi Assumons que la génération de l'URL de la vidéo ou le téléchargement de la vidéo soit réussi Assumons que la génération de l'URL de la vidéo ou le téléchargement de la vidéo soit réussi''',
            })
        else:
            # Return error response if any field is missing or failed
            return JsonResponse({
                'status': 'error',
                'message': 'Failed to process the video.'
            })

    # Render the form template
    return render(request, 'index.html')


def generate_video(request):
    if request.method == 'POST':
        # Assuming file and other form data is captured (as explained earlier)
        uploaded_file = request.FILES.get('file_upload')
        textarea_value = request.POST.get('textarea_field')
        game_type = request.POST.get('game_type')

        text_english = request.POST.get('text_english')
        text_french = request.POST.get('text_french')

        print(uploaded_file)
        print(textarea_value)
        print(game_type)
        print(text_english)
        print(text_french)

        # Add your logic to handle the uploaded file and process the video
        if uploaded_file and textarea_value and game_type:
            # Assuming video URL generation or video upload is successful
            # Replace with actual video URL
            video_url = 'https://www.youtube.com/embed/6zEkCNPF664'

            # Return success response with video URL
            return JsonResponse({
                'status': 'success',
                'video_url': video_url,
            })
        else:
            # Return error response if any field is missing or failed
            return JsonResponse({
                'status': 'error',
                'message': 'Failed to process the video.'
            })

    # Render the form template
    return render(request, 'index.html')

from django.shortcuts import render
from django.http import JsonResponse



def index(request):
    return render(request, 'index.html')




def upload(request):
    if request.method == 'POST':
        # Assuming file and other form data is captured (as explained earlier)
        uploaded_file = request.FILES.get('file_upload')
        textarea_value = request.POST.get('textarea_field')
        game_type = request.POST.get('game_type')

        print (uploaded_file) 
        print (textarea_value) 
        print (game_type) 

        

        # Add your logic to handle the uploaded file and process the video
        if uploaded_file and textarea_value and game_type:

            # Return success response with video URL
            return JsonResponse({
                'status': 'success',
                'generated_text': '''Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successfulAssuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful, Assuming video URL generation or video upload is successful''',
                # Return the uploaded form data for reuse
                'uploaded_file_name': uploaded_file.name if uploaded_file else None,
                'textarea_value': textarea_value,
                'game_type': game_type,
            })
        else:
            # Return error response if any field is missing or failed
            return JsonResponse({
                'status': 'error',
                'message': 'Failed to process the video.'
            })

    # Render the form template
    return render(request, 'index.html')




def generate_french(request):
    if request.method == 'POST':
        # Assuming file and other form data is captured (as explained earlier)
        generated_text_data = request.POST.get('generated_text_data')

        print (generated_text_data) 
       
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


        print (uploaded_file) 
        print (textarea_value) 
        print (game_type) 
        print (text_english) 
        print (text_french) 


        # Add your logic to handle the uploaded file and process the video
        if uploaded_file and textarea_value and game_type:
            # Assuming video URL generation or video upload is successful
            video_url = 'https://www.youtube.com/embed/6zEkCNPF664'  # Replace with actual video URL

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

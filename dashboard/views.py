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

        # from IPython import embed 
        # embed()

        import time
        # Add a delay of 5 seconds
        time.sleep(5)
        # Code after the delay will execute
        print("This message is shown after a 5-second delay")

        # Add your logic to handle the uploaded file and process the video
        if uploaded_file and textarea_value and game_type:
            # Assuming video URL generation or video upload is successful
            video_url = 'https://www.youtube.com/embed/6zEkCNPF664'  # Replace with actual video URL

            # Return success response with video URL
            return JsonResponse({
                'status': 'success',
                'video_url': video_url
            })
        else:
            # Return error response if any field is missing or failed
            return JsonResponse({
                'status': 'error',
                'message': 'Failed to process the video.'
            })

    # Render the form template
    return render(request, 'index.html')
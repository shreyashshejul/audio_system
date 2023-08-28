from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UploadedAudio

def upload_audio(request):
    user = 'User1'  # Replace with user authentication
    total_duration = 0
    
    if request.method == 'POST':
        files = request.FILES.getlist('audio_files')
        
        for file in files:
            extension = file.name.split('.')[-1]
            duration = 0
            file_size = 0
            
            try:
                # Calculate the duration and file size here using your API
                # Replace the following lines with your actual calculations
                duration = 5.0  # Example duration in minutes
                file_size = file.size
                
                if duration > 10:
                    # Generate a warning here
                    pass
                
                uploaded_audio = UploadedAudio(
                    user=user,
                    file=file,
                    extension=extension,
                    duration=duration,
                    file_size=file_size
                )
                uploaded_audio.save()
                
                # Add the duration to the total
                total_duration += duration
                messages.success(request, f"Song :- '{file.name}' successfully uploaded.")
            except Exception as e:
                print(f"Error processing file: {str(e)}")

    audios = UploadedAudio.objects.filter(user='User1')  # Replace with user authentication
    return render(request, 'upload_audio.html', {'audios': audios, 'total_duration': total_duration})


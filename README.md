
# Project Title - Audio System

A brief description of what this project does and who it's for
The Shreyash Audio Manager is a web application built with Django that simplifies audio file management. It provides a user-friendly dashboard for users to upload and enjoy their audio files free. Whether you're a music enthusiast or need to manage audio content, this application streamlines the process.

## Features


- **User-Friendly Dashboard**: A user-friendly dashboard provides easy access to all audio management features.

- **Upload Audio Files**: Users can upload audio files directly from their device.

- **File Information**: The system automatically extracts and displays file information, including file name, upload date, extension, duration, and file size.

- **Audio Playback**: Users can listen to uploaded audio files directly within the application.

- **Warning System**: Warns users if the total duration of uploaded files exceeds a specified limit (e.g., 10 minutes).

- **User Authentication**: Implement user authentication to secure uploaded audio files and associate them with specific users.

## Getting Started

## Installation

To set up and run the Shreyash Audio Manager project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/shreyashshejul/audio-manager-shreyash.git
   cd audio-manager-shreyash
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use:venv\Scripts\activate
3. Install project dependencies:
    ```bash
    pip install -r requirements.txt
4. Run database migrations:
    ```bash
    python manage.py migrate
5. Create a superuser account (for admin access):
    ```bash
    python manage.py createsuperuser
6. Start the development server:
    ```bash
    python manage.py runserver
7.  Access the application at http://localhost:8000/admin/ for admin access and http://localhost:8000/audio/upload/ to upload audio files.

You can log in with the superuser account created earlier to access admin features.
## Tech Stack

**Client:** 
- HTML
- CSS
- JavaScript


**Server:** 
- Python
- Django
- Database


## Authors

- [@shreyashshejul](https://www.github.com/shreyashshejul)


# Hi, I'm Shreyash! 👋


## 🚀 About Me
I'm a full stack developer...
## License

[MIT](https://choosealicense.com/licenses/mit/)


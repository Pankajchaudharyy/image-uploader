# Django Image Uploader

A Django application that allows users to upload images, view them in a gallery, and delete them if needed.

## Features

- User authentication and registration
- Image upload functionality
- Display uploaded images in a gallery
- Delete images from the gallery

## Requirements

- Python 3.x
- Django 3.x or higher
- Pillow library for image handling

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations and start the server:**

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Register a new user or log in with an existing account.
3. Upload images through the provided form.
4. View uploaded images in the gallery.
5. Delete images if necessary.

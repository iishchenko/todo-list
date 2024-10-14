# todo-list

# Django Todo List Project

A simple Todo List application built with Django that allows users to manage tasks and tags. Tasks can be created with optional deadlines and marked as done when completed.

## Features

- Add, view, and manage tasks
- Add and view tags
- Sidebar navigation for ease of use
- Tasks ordered by completion status and creation date

## Requirements

- Python 3.x
- Django 4.x
- PostgreSQL (or SQLite as default, if you prefer)

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/your-username/todo-list.git
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate  # For Windows
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4.Apply the migrations:
    ```
    python manage.py migrate
    ```

5.Create a superuser for the admin panel:
    ```
    python manage.py createsuperuser
    ```

6.Start the development server:
    ```
    python manage.py runserver
    ```

7.Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Usage

### Home Page
- Displays a list of tasks ordered by their status (not done first, then done) and by creation date (newest first).

### Tag Management
- Navigate to `http://127.0.0.1:8000/tags/` to view, add, and delete tags.

### Task Management
- Add a new task by navigating to `http://127.0.0.1:8000/tasks/add/`.

## Folder Structure


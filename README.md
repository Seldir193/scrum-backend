# Scrum Backend Project

## Project Description
This project is a Django REST API backend designed to manage tasks and contacts in a Scrum-like workflow system.

## Features
- User registration and authentication (JWT)
- CRUD operations for tasks and contacts
- Task filtering by status (To Do, In Progress, Done)
- RESTful API with Django REST Framework

## Prerequisites
- Python 3.x
- Django
- Git

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Seldir193/scrum-backend.git
    ```

2. Navigate into the project directory:
    ```bash
    cd scrum-backend
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Mac/Linux
    .\venv\Scripts\activate   # For Windows
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

7. Start the local server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication
- **POST** `/api/login/`: Login and obtain JWT tokens.
- **POST** `/api/register/`: Register a new user.
- **POST** `/api/logout/`: Log out the current user.
- **POST** `/api/token/`: Obtain JWT token.
- **POST** `/api/token/refresh/`: Refresh JWT token.

### Tasks
- **GET** `/api/tasks/`: Get a list of tasks.
- **POST** `/api/tasks/`: Create a new task.
- **PUT** `/api/tasks/<id>/`: Update a task.
- **DELETE** `/api/tasks/<id>/`: Delete a task.

## Running Tests

Unit tests are available for the following areas:
- **Task Model Tests**: Ensures that tasks are correctly created and updated.
- **Contact Model Tests**: Tests related to contact creation and management.
- **Task API Tests**: Verifies CRUD operations for tasks through the API.
- **Authentication Tests**: Ensures login, registration, and logout functionalities work as expected.

To run the tests, use the following command:
```bash
python manage.py test

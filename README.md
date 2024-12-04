# FastAPI Social Media Backend

A comprehensive social media backend using FastAPI, featuring user authentication, CRUD operations, PostgreSQL integration, and JWT authentication. Includes Docker for containerization and GitHub Actions for CI/CD.

![bb](https://github.com/user-attachments/assets/f349d276-f57b-438f-ae52-1108c6b7943c)


## Database Design
![Screenshot 2024-12-04 205411](https://github.com/user-attachments/assets/2c7ff675-783d-4d31-899a-24f90bb7381d)

## Features

- FastAPI for building and managing the API endpoints.
- Pydantic for schema validation and data parsing.
- SQLAlchemy for ORM and database interactions.
- PostgreSQL for data storage.
- JWT for secure user authentication and authorization.
- Alembic for database migrations.
- Pytest for thorough testing of the API.
- Docker for containerization and easy deployment.
- GitHub Actions for CI/CD pipeline integration.
- Deployment configurations for both Heroku and Ubuntu with NGINX.

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Pytest
- Alembic

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-social-backend.git
   cd fastapi-social-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   alembic upgrade head
   ```

## Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```

## Running Tests

To run the tests using Pytest:
```bash
pytest
```

## Deployment

### Docker

1. Build the Docker image:
   ```bash
   docker build -t fastapi-social-backend .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 fastapi-social-backend
   ```



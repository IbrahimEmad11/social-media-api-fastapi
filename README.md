# FastAPI Social Media Backend

A comprehensive social media backend using FastAPI, featuring user authentication, CRUD operations, PostgreSQL integration, and JWT authentication. Includes Docker for containerization and GitHub Actions for CI/CD.

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
   git clone https://github.com/yourusername/fastapi-social-backend.git
   cd fastapi-social-backend
   

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
   pip install -r requirements.txt


4. Set up the database:
   ```bash
   alembic upgrade head
   ```

## Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The API documentation will be available at:
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

### Heroku

1. Create a Heroku app and add a PostgreSQL database.
2. Push the code to Heroku:
   ```bash
   git push heroku main
   ```
3. Run database migrations:
   ```bash
   heroku run alembic upgrade head
   ```

## License

This project is licensed under the MIT License.
```

This README provides a concise overview of the project, its features, installation steps, and how to run and deploy the application.

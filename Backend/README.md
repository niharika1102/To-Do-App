# Todo Application Backend

A robust REST API backend built with FastAPI and PostgreSQL for the Todo application. This backend provides all necessary endpoints for managing todo items with full CRUD functionality.

## Technologies Used

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

## Project Structure

- `main.py`: The main FastAPI application file and route definitions.
- `models.py`: The SQLAlchemy and Pydantic models.
- `services.py`: Business logic and databse operations for the application.

## Prerequisites

- Python 3.7+
- PostgreSQL
- pip (Python package manager)

## Setup and Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install fastapi sqlalchemy psycopg2-binary uvicorn pydantic
```

3. Configure PostgreSQL:
- Ensure PostgreSQL is running
- Update the connection string in `models.py` if needed:
```python
CONNECTION_STRING = "postgresql://temporal:temporal@localhost:5432/postgres"
```

4. Run the application:
```bash
python main.py
```

## API Endpoints

### GET `/`
- Welcome message
- Response: String

### GET `/todos/`
- Retrieve all todos
- Response: List of TodoResponse objects

### GET `/todos/{id}`
- Retrieve a specific todo
- Parameters: id (integer)
- Response: TodoResponse object

### POST `/todos/`
- Create a new todo
- Request Body: TodoCreate object
- Response: TodoResponse object

### PUT `/todos/{id}`
- Update an existing todo
- Parameters: id (integer)
- Request Body: TodoUpdate object
- Response: TodoResponse object

### DELETE `/todos/{id}`
- Delete a todo
- Parameters: id (integer)
- Response: Success message

## Data Models

### TodoBase (Pydantic Model)
```python
{
    "id": Optional[int],
    "title": str,
    "completed": bool
}
```

### Database Schema
```sql
CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    title VARCHAR,
    completed BOOLEAN DEFAULT FALSE
);
```

## Error Handling

The API implements proper error handling for:
- 404 Not Found
- 400 Bad Request
- 500 Internal Server Error

## CORS

CORS is enabled for all origins with the following settings:
- All origins allowed (`"*"`)
- All methods allowed
- All headers allowed
- Credentials supported

## Development

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Document functions and classes

## Database Management

The application uses SQLAlchemy ORM with the following features:
- Automatic table creation
- Session management
- Transaction handling
- Connection pooling

## Real life examples of Restful APIs
1. Social Media APIs:
- Twitter API
- Instagram API

2. E-commerce APIs:
- Amazon API
- Shopify API

3. Banking APIs:
- Razorpay API

4. Entertainment APIs:
- Spotify API
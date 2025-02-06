# Employee Management API with Django

## Project Overview

This project demonstrates how to build a **RESTful API** for managing employee records using **Django** and **Django REST Framework (DRF)**. The API supports CRUD operations for employee management, including adding, retrieving, updating, and deleting employees.

## Features

- **Employee Model**: Stores employee details such as name, email, department, salary, and joining date.
- **API Endpoints**:
    - `POST /api/employees/`: Add a new employee.
    - `GET /api/employees/`: Retrieve all employees.
    - `GET /api/employees/{id}/`: Retrieve a specific employee by ID.
    - `PUT /api/employees/{id}/`: Update an employee's details.
    - `DELETE /api/employees/{id}/`: Delete an employee.
- **Validation**: Ensures valid data for attributes like name, email, salary, etc.
- **Error Handling**: Handles errors such as not found or invalid data.
- **Logging**: Logs events related to employee creation, update, and deletion.
- **Testing**: Includes unit and integration tests to validate the functionality.

## Project Setup

### Prerequisites

Ensure that you have the following installed:

- Python 3.8 or higher.
- Django 4.0+
- Django REST Framework 3.12+

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/employee-api.git
    cd employee-api
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
   

4. **Install dependencies**:
    
5. **Run migrations** to set up the database:
    ```bash
    python manage.py migrate
    ```

### Running the Application

Start the Django development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/api/`.

### Testing the API

- You can test the API using **Postman** or any other API testing tool, or access the interactive API documentation at `http://127.0.0.1:8000/docs/`.

- Unit tests are included. To run them, use:
    ```bash
    pytest
    ```

## API Endpoints

### 1. **Create Employee**

- **URL**: `/api/employees/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "department": "HR",
        "salary": 50000,
        "joining_date": "2022-01-01"
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "department": "HR",
        "salary": 50000,
        "joining_date": "2022-01-01"
    }
    ```

### 2. **Get All Employees**

- **URL**: `/api/employees/`
- **Method**: `GET`
- **Response**:
    ```json
    [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "department": "HR",
            "salary": 50000,
            "joining_date": "2022-01-01"
        },
        ...
    ]
    ```

### 3. **Get Employee by ID**

- **URL**: `/api/employees/{id}/`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "department": "HR",
        "salary": 50000,
        "joining_date": "2022-01-01"
    }
    ```

### 4. **Update Employee Details**

- **URL**: `/api/employees/update/`
- **Method**: `PUT`
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@newemail.com",
        "department": "Finance",
        "salary": 60000,
        "joining_date": "2022-01-01"
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@newemail.com",
        "department": "Finance",
        "salary": 60000,
        "joining_date": "2022-01-01"
    }
    ```

### 5. **Delete Employee**

- **URL**: `/api/employees/delete/`
- **Method**: `DELETE`
- **Response**:
    ```json
    {
        "message": "Employee deleted successfully"
    }
    ```

## Testing

- The project uses **pytest** for testing. The tests are located in the `employees/tests/` directory.
- To run the tests:
    ```bash
    pytest
    ```

### Test Cases

- CRUD operations for adding, retrieving, updating, and deleting employees.
- Validations for ensuring correct employee data.
- Error handling tests for cases like employee not found.

## Logging

The application uses Python's `logging` module to log key events, such as when an employee is created, updated, or deleted.

## Dockerization (Optional)

You can containerize the application using Docker by building the image with the provided **Dockerfile** and running the application in a Docker container.


### Conclusion

This project provides a full-featured **Employee Management System API** built with **Django** and **Django REST Framework**. It covers CRUD operations, error handling, data validation, and testing, as well as advanced features like logging and Dockerization.


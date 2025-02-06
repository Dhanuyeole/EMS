import pytest
import httpx
from rest_framework import status

BASE_URL = "http://127.0.0.1:8000/api/"

# Test for creating an employee
@pytest.mark.asyncio
async def test_create_employee_route():
    data = {
        "name": "Jane Doe",
        "email": "jane531@example.com",
        "department": "Finance",
        "salary": 60000,
        "joining_date": "2022-01-01"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}employees/create/", json=data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == data["name"]
    assert response.json()["email"] == data["email"]


# Test for retrieving an employee by ID
@pytest.mark.asyncio
async def test_get_employee_route():
    employee_id = 5  # Assuming an employee with this ID exists

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}employees/{employee_id}/")

    assert response.status_code == status.HTTP_200_OK
    assert "name" in response.json()
    assert "email" in response.json()


# Test for updating an employee
@pytest.mark.asyncio
async def test_update_employee_route():
    employee_id = 6  # Assuming an employee with this ID exists
    # New data for updating the employee
    updated_data = {
        "emp_id": employee_id,
        "emp_data": {
            "name": "Jane Doe",
            "email": "jane454456@example.com",
            "department": "Finance",
            "salary": 60000,
            "joining_date": "2022-02-01"
        }
    }

    # Sending the PUT request to update the employee
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}employees/update/", json=updated_data)

    # Assert the response
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == updated_data["emp_data"]["name"]
    assert response.json()["email"] == updated_data["emp_data"]["email"]
    assert response.json()["department"] == updated_data["emp_data"]["department"]
    assert response.json()["salary"] == updated_data["emp_data"]["salary"]
    assert response.json()["joining_date"] == updated_data["emp_data"]["joining_date"]

# Test for deleting an employee
@pytest.mark.asyncio
async def test_delete_employee_route():
    employee_id = 4

    # Send the DELETE request to delete the employee using query parameters
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}employees/delete/", params={"emp_id": employee_id})

    # Assert the response
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.json() == {"message": "Employee deleted successfully"}

    # Verify that the employee is deleted from the database
    # Try to fetch the employee and expect a 404 error (not found)
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}employees/{employee_id}/")
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
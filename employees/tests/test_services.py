# employees/tests/test_services.py

import pytest
from employees.services import create_employee, get_employee, update_employee,delete_employee
from employees.models import Employee

@pytest.mark.django_db
def test_create_employee():
    name = "John Doe"
    email = "john@example.com"
    department = "HR"
    salary = 50000
    joining_date = "2022-01-01"

    # Call the service function
    employee = create_employee(name, email, department, salary, joining_date)

    # Check that the employee has been created
    assert employee.name == name
    assert employee.email == email
    assert employee.department == department
    assert employee.salary == salary
    assert employee.joining_date == joining_date

# Read Employee Service Test
@pytest.mark.django_db
def test_get_employee():
    # First, create an employee
    name = "Jane Doe"
    email = "jane@example.com"
    department = "Finance"
    salary = 60000
    joining_date = "2023-02-01"
    
    employee = create_employee(name, email, department, salary, joining_date)
    
    # Call the service function
    fetched_employee = get_employee(employee.pk)

    # Check that the employee fetched has the same data as the created employee
    assert fetched_employee is not None
    assert fetched_employee.name == name
    assert fetched_employee.email == email
    assert fetched_employee.department == department
    assert fetched_employee.salary == salary
    assert str(fetched_employee.joining_date) == joining_date


# Update Employee Service Test
@pytest.mark.django_db
def test_update_employee():
    # First, create an employee
    name = "David Smith"
    email = "david@example.com"
    department = "IT"
    salary = 70000
    joining_date = "2021-05-01"
    
    employee = create_employee(name, email, department, salary, joining_date)

    # Update employee's department and salary using the service
    updated_department = "Marketing"
    updated_salary = 75000
    updated_employee = update_employee(employee.pk, department=updated_department, salary=updated_salary)

    # Check that the employee has been updated
    assert updated_employee.department == updated_department
    assert updated_employee.salary == updated_salary


# Delete Employee Service Test
@pytest.mark.django_db
def test_delete_employee():
    # First, create an employee
    name = "Michael Jordan"
    email = "michael@example.com"
    department = "Sales"
    salary = 80000
    joining_date = "2020-08-15"
    
    employee = create_employee(name, email, department, salary, joining_date)

    # Call the service function to delete the employee
    deletion_result = delete_employee(employee.pk)

    # Check that the employee was deleted
    assert deletion_result is True
    # Ensure the employee no longer exists in the database
    assert Employee.objects.filter(pk=employee.pk).count() == 0
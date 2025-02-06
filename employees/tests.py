from django.test import TestCase
from .models import Employee

class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(name="John Doe", email="john@example.com", department="IT", salary=50000, joining_date="2024-01-10")

    def test_employee_creation(self):
        employee = Employee.objects.get(name="John Doe")
        self.assertEqual(employee.salary, 50000)

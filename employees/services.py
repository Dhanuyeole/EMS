from .models import Employee

def create_employee(name, email, department, salary, joining_date):
    employee = Employee.objects.create(
        name=name, 
        email=email, 
        department=department, 
        salary=salary, 
        joining_date=joining_date
    )
    return employee

def get_employee(pk):
    try:
        employee = Employee.objects.get(pk=pk)
        return employee
    except Employee.DoesNotExist:
        return None

def update_employee(pk, name=None, email=None, department=None, salary=None, joining_date=None):
    try:
        employee = Employee.objects.get(pk=pk)
        if name:
            employee.name = name
        if email:
            employee.email = email
        if department:
            employee.department = department
        if salary:
            employee.salary = salary
        if joining_date:
            employee.joining_date = joining_date
        employee.save()
        return employee
    except Employee.DoesNotExist:
        return None

def delete_employee(pk):
    try:
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return True
    except Employee.DoesNotExist:
        return False

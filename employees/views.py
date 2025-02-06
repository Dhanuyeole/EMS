from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination
import logging

# Create a logger instance for employee events
logger = logging.getLogger('employee')

class EmployeePagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'  # Clients can use this to override the page size
    max_page_size = 100  # Maximum page size

class EmployeeListView(APIView):
    """
    This view allows you to list all employees and create a new employee.
    - GET: List all employees with pagination and sorting.
    - POST: Create a new employee.
    """
    def get(self, request):
        employees = Employee.objects.all()

        # Handle sorting
        ordering = request.query_params.get('ordering', 'name')  # Default ordering by 'name'
        employees = employees.order_by(ordering)

        # Paginate the employees
        paginator = EmployeePagination()
        paginated_employees = paginator.paginate_queryset(employees, request)
        
        # Log the event: employee list retrieved
        logger.info(f"Retrieved employee list with {len(paginated_employees)} employees, sorted by {ordering}.")

        # Serialize and return paginated data
        serializer = EmployeeSerializer(paginated_employees, many=True)
        return paginator.get_paginated_response(serializer.data)

class EmployeeCreateView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            logger.info(f"New employee created: {employee.name}, ID: {employee.id}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Log the event: failed employee creation
        logger.warning(f"Failed to create employee: {request.data}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeRetrieveView(APIView):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)

         # Log the event: employee retrieved
        logger.info(f"Retrieved employee details: {employee.name}, ID: {employee.id}")

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

class EmployeeUpdateView(APIView):
    def put(self, request):
        employee = get_object_or_404(Employee, pk=request.data.get('emp_id'))
        serializer = EmployeeSerializer(employee, data=request.data.get('emp_data'), partial=True)
        if serializer.is_valid():
            updated_employee = serializer.save()
            # Log the event: employee updated
            logger.info(f"Updated employee: {updated_employee.name}, ID: {updated_employee.id}")
            return Response(serializer.data)
        # Log the event: failed employee update
        logger.warning(f"Failed to update employee with ID {request.data.get('emp_id')}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDeleteView(APIView):
    def delete(self, request):
        employee = get_object_or_404(Employee, pk=request.data.get('emp_id'))
        employee_name = employee.name
        employee.delete()
        # Log the event: employee deleted
        logger.info(f"Deleted employee: {employee_name}, ID: {employee.id}")
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


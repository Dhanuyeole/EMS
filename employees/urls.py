from django.urls import path
from .views import (
    EmployeeListView, EmployeeCreateView,
    EmployeeRetrieveView, EmployeeUpdateView, EmployeeDeleteView
)


urlpatterns = [
    path("employees/", EmployeeListView.as_view(), name="employee-list"),   # GET all employees
    path("employees/create/", EmployeeCreateView.as_view(), name="employee-create"),  # POST new employee
    path("employees/<int:pk>/", EmployeeRetrieveView.as_view(), name="employee-retrieve"),  # GET single employee
    path("employees/update/", EmployeeUpdateView.as_view(), name="employee-update"),  # PUT update employee
    path("employees/delete/", EmployeeDeleteView.as_view(), name="employee-delete"),  # DELETE employee
]

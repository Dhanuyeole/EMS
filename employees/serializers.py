from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'help_text': 'Full name of the employee'},
            'email': {'help_text': 'Employee’s unique email address'},
            'salary': {'help_text': 'Annual salary of the employee'},
        }

        
    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be a positive number.")
        return value
    
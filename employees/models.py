from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    salary = models.FloatField()
    joining_date = models.DateField()

    def __str__(self):
        return self.name

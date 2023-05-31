from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email= models.EmailField()
    phone= models.CharField(max_length=10)
    
class Employees(models.Model):
    employeeid=models.IntegerField()
    employeename=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    Designation=models.CharField(max_length=10)
    place=models.CharField(max_length=20)
    salary=models.IntegerField()
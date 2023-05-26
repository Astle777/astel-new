from django.db import models

# Create your models here.
class stud(models.Model):
    name=models.CharField(max_length=26)
    rollno=models.IntegerField()

class collage(models.Model):
    Dptname=models.CharField(max_length=26)
    Collagename=models.CharField(max_length=26)
    Pincode=models.IntegerField()
from django.db import models

# Create your models here.

class item(models.Model):
    image=models.ImageField(upload_to='product')
    title=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    title1=models.CharField(max_length=200)
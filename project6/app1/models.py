from django.db import models
class Book(models.Model):
 Ttle=models.CharField(max_length=20)
 Author=models.CharField(max_length=20)
 pdf=models.FileField(upload_to='book/pdf')
 cover=models.ImageField(upload_to='book/cover',null=True,blank=True)
    

# Create your models here.

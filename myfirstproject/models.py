from django.db import models

# Create your models here.
class student(models.Model):
    fname=models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50,default="0")
    password = models.CharField(max_length=20,default="0")
    city = models.TextField(max_length=20)
    contact=models.IntegerField(max_length=20)

from django.db import models
from rest_framework import serializers

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    
class Studentserializers(serializers.ModelSerializer) :
    class Meta: 
        model=Student
        fields=['name','address']  
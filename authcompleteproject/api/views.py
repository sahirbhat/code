from django.shortcuts import render
from . models import Student
from . models import Studentserializers
from rest_framework import viewsets

# Create your views here.
class Studentviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializers
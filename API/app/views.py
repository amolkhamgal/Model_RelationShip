from django.shortcuts import render
from .models import Author,Book,Student,Course
from .serializers import AuthorSerializer,BookSerializer,StudentSerializer,CourseSerializer
from rest_framework import viewsets
# Create your views here.


class AuthorData(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    
class BookData(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer    
    
    

class StudentData(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class CourseData(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer     

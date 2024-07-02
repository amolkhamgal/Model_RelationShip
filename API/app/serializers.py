from rest_framework import serializers
from .models import Author,Book,Student,Course


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model=Author
        fields="__all__"

class BookSerializer(serializers.Serializer):
    class Meta:
        model=Book
        fields="__all__"       
        
class StudentSerializer(serializers.Serializer):
    class Meta:
        model=Student
        fields="__all__"

class CourseSerializer(serializers.Serializer):
    class Meta:
        model=Course
        fields="__all__"            
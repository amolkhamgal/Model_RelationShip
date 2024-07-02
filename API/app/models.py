from django.db import models

# Create your models here.

class Author(models.Model):
    author_id=models.IntegerField(primary_key=True,auto_created=True)
    author_name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.author_name
    
class Book(models.Model):
    book_name=models.CharField(max_length=40)
    author=models.ForeignKey(Author ,related_name='book_set' ,on_delete=models.CASCADE)   
    
    def __str__(self):
        return self.book_name 
    
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.title
    
    
    
    

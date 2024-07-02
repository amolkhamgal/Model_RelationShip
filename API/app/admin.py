from django.contrib import admin
from .models import Author,Book,Student,Course
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=["author_id","author_name"]
admin.site.register(Author,AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display=["book_name","author"]
admin.site.register(Book,BookAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=["name","age","email"]
admin.site.register(Student,StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=["title","code","description"]
admin.site.register(Course,CourseAdmin)

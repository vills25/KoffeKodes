from django.contrib import admin
from .models import Student, Faculty, Mark, Subject,User

# Register your models here. 
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Mark)
admin.site.register(Subject)
admin.site.register(User)
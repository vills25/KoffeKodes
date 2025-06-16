from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = ( 
    ('student', 'Student'),
    ('faculty', 'Faculty'),
)

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_class = models.CharField(max_length=100)
    subjects = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name
    
class Product(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return self.name
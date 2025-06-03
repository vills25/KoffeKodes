from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    age  = models.IntegerField(default= None)
    address = models.TextField(blank = True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name  

class Car(models.Model):
    car_name = models.CharField(max_length = 100)
    speed = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.car_name    
         
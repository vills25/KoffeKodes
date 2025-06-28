from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length= 100)
    course= models.CharField(max_length= 100)
    email = models.EmailField(blank=False)
    phone = models.IntegerField(blank=False)

    def __self__(self):
        return self.name
    
    
from django.db import models
from django.forms import ValidationError

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    contact = models.CharField(max_length=13)
    age = models.IntegerField(null = True)
    total_patient = models.IntegerField(default=0)
    summary = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name

    def validate(self, data):
        if data['age'] < 18:
            raise ValidationError("Must be 18 or older to register.")
        return data
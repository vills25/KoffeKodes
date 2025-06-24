from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=50)
    contact = models.CharField(max_length=255)
    total_patient = models.IntegerField(default=0)
    summary = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name

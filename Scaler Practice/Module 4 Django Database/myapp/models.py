from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length= 255)
    degree = models.CharField(max_length=50)
    contact = models.CharField(max_length=255)
    total_patient = models.IntegerField(default=0)
    summary = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name

class ReportType(models.Model):
    name = models.CharField(max_length=255)
    report_charge = models.FloatField()

    def __str__(self):
        return self.name 

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    total_amount = models.FloatField(blank = True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# ORM(Object Relational Mapping)
# python manage.py shell

# from myapp.models import Doctor,ReportType, Patient
# >>> ReportType.objects.create(name='Fever', report_charge='200')
# >>> a.save()

# using queryset getting data from database, with options, Get, filter, all, delete
# To get data in decending put ' - ' before the key name, ex. -report_charge

#  >>> ReportType.objects.all()     
#  <QuerySet [<ReportType: Malaria>, <ReportType: COVID-19>, <ReportType: Fever>]>

# >>> ReportType.objects.get(pk = 1)
# <ReportType: Malaria>

 # values_list() returns only column lists ppf table

 

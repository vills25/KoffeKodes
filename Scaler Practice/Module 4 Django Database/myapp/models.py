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
# ex. 
    #  Doctor.objects.all().order_by('-name').values()      
    # <QuerySet [{'id': 1, 'name': 'Vishal', 'degree': 'B.H.M.S.', 'contact': '473027290011', 'total_patient': 5, 'summary': 'helo helo helo', 'address': 'Surat'}, {'id': 2, 'name': 'Neet', 'degree': 'MBBS', 'contact': '8451269512', 'total_patient': 5, 'summary': 'hehehehehehe', 'address': 'Ahmedabad'}, {'id': 3, 'name': 'Neet', 'degree': 'MBBS', 'contact': '8451269512', 'total_patient': 5, 'summary': 'hehehehehehe', 'address': 'Ahmedabad'}, {'id': 5, 'name': 'Mehul', 'degree': 'BHMS', 'contact': '8451269512', 'total_patient': 10, 'summary': 'hehehehehehe', 'address': 'Pune'}, {'id': 4, 'name': 'Karan', 'degree': 'BHMS', 'contact': '8451269512', 'total_patient': 4, 'summary': 'hehehehehehe', 'address': 'Mumbai'}]>
    # >>> Doctor.objects.all().order_by('name').values()  
    # <QuerySet [{'id': 4, 'name': 'Karan', 'degree': 'BHMS', 'contact': '8451269512', 'total_patient': 4, 'summary': 'hehehehehehe', 'address': 'Mumbai'}, {'id': 5, 'name': 'Mehul', 'degree': 'BHMS', 'contact': '8451269512', 'total_patient': 10, 'summary': 'hehehehehehe', 'address': 'Pune'}, {'id': 2, 'name': 'Neet', 'degree': 'MBBS', 'contact': '8451269512', 'total_patient': 5, 'summary': 'hehehehehehe', 'address': 'Ahmedabad'}, {'id': 3, 'name': 'Neet', 'degree': 'MBBS', 'contact': '8451269512', 'total_patient': 5, 'summary': 'hehehehehehe', 'address': 'Ahmedabad'}, {'id': 1, 'name': 'Vishal', 'degree': 'B.H.M.S.', 'contact': '473027290011', 'total_patient': 5, 'summary': 'helo helo helo', 'address': 'Surat'}]>

#  >>> ReportType.objects.all()
#  <QuerySet [<ReportType: Malaria>, <ReportType: COVID-19>, <ReportType: Fever>]>

# >>> ReportType.objects.get(pk = 1)
# <ReportType: Malaria>

 # values_list() returns only column lists ppf table

# aggregate in queryset
# >>> from django.db.models import Sum, Max, Min, Count, Avg
# >>> ReportType.objects.aggregate(Sum('report_charge'))
# {'report_charge__sum': 2200.0}
 
 # annotate in queryset
# ReportType.objects.values('name').annotate(Sum('report_charge'))
# <QuerySet [{'name': 'Malaria', 'report_charge__sum': 500.0}, {'name': 'COVID-19', 'report_charge__sum': 1500.0}, {'name': 'Fever', 'report_charge__sum': 200.0}]>

# Filter using OR
# we can get objects with multiple filter using OR 
# >>> Doctor.objects.filter(degree='MBBS') | Doctor.objects.filter(name='neet')      
# <QuerySet [<Doctor: Neet>, <Doctor: Neet>]>

# Django transections
# A transaction in Django means group of database operations that function as a single atomic unit—either all operations success, or none of them.
# atomic() ensures that all operation within function block works successful, if one of them fails, it will rollback all transections.
# for ex. atomic() can be used for money transection.
# we can writes atomic() inside the def func as transection.atomic() or we can write as decorator @transection.atomic() abpve the function.
# Transactions can be nested, with creating savepoints. if inner block fails, it rolls back to its savepoint without touching the outer transaction.

# SQL is a query language that is used mostly in all databases. 
# With the help of SQL, users can access, manipulate the data in the relational database management system., create tables and databases and also drop tables and databases.

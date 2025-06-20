from django.contrib import admin
from .models import Doctor, ReportType, Patient

admin.site.register(Doctor)
admin.site.register(ReportType)
admin.site.register(Patient)

# Register your models here.

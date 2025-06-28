from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'degree', 'contact','age' ,'total_patient','summary', 'address')
        # We can also specify the read_only_fields, instead adding the read only=True attribute to each field
        #read_only_fields = ('degree')
        #write_only_fields = ('degree')
        
        
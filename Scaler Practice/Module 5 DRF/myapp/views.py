from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    # def delete_objects(self, request):
    #     Doctor.objects.all().delete()

    #     return Response({"message":"Deleted"}, status= 201)
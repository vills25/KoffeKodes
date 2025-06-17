from rest_framework import serializers
from .models import Product, Category
from django.contrib.auth import get_user_model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.username')
    class Meta:
        model = Product
        fields = '__all__'



    
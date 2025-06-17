from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.PrimaryKeyRelatedField( queryset=Category.objects.all(), source='category', write_only=True)
    vendor = serializers.CharField(source='vendor.username', read_only=True)

    class Meta:
        model = Product
        fields = [ 'id', 'vendor', 'name', 'description', 'price', 'image', 'created_at', 'category', 'category_id' ]

    
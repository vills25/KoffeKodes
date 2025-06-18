from rest_framework import serializers
from .models import Product, Category, Cart

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.PrimaryKeyRelatedField( queryset=Category.objects.all(), source='category', write_only=True)
    vendor = serializers.CharField(source='vendor.username', read_only=True)

    class Meta:
        model = Product
        fields = [ 'id', 'vendor', 'name', 'description', 'price', 'image', 'created_at', 'category', 'category_id' ]
        read_only_fields = ['id', 'created_at', 'vendor']

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['product', 'product_name', 'price', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cartitem_set', many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items', 'total_price']

    def get_total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.cartitem_set.all())


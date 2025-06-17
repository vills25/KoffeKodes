from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission

class IsVendorOrReadOnly(BasePermission):
    def permission(self, request, obj): # Check if the user is the vendor and has permission to edit/delete the product
        if request.method in ['GET']:# Allow read-only access for all users and restrict write access to vendors only
            return True 
        return obj.vendor == request.user # Allow write access only to the vendor of the product

class ProductViewSet(viewsets.ModelViewSet): # CRUD operations, filtering, searching, and throttling, 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # Serializer class to convert model instances to JSON, instance means the data that will be serialized and sent to the client
    permission_classes = [IsAuthenticatedOrReadOnly, IsVendorOrReadOnly] 
    filterset_fields = ['category', 'vendor']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']
    throttle_scope = 'product-list'
    
    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
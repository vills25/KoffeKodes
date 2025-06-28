from .views import get_customers,customer_create, get_one_customer, update_customer, delete_customer
from django.urls import path
urlpatterns = [
    
    path('customers/', get_customers ),
    path('customers/create/', customer_create),
    path('customers/one_customer/', get_one_customer),
    path('customers/edit/', update_customer ),
    path('customers/delete/', delete_customer ),
]

from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    path('items/add/', views.item_create, name='add_item'),
    path('items/<int:pk>/edit/', views.item_update, name='edit_item'),
    path('items/<int:pk>/delete/', views.item_delete, name='delete_item'),
]
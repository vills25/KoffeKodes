from django.urls import path
from .views import *

urlpatterns = [
    path('items/', item_list),
    path('items/details-fetch/', item_detail),
    path('items/add/', item_create),
    path('items/edit/', item_update),
    path('items/delete/', item_delete),
    
]
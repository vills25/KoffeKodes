from django.urls import path
from . import views

urlpatterns = [
    path('create_receipe/', views.create_receipes),
    path('receipe_detail/', views.receipe_detail),
    path('delete_receipe/', views.delete_receipes),
    path('update_receipe/', views.update_receipe),

]
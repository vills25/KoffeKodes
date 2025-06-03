from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='base'),
     path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('success_page/', views.success_page , name='success_page'),
]
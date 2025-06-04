"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from myapp.views import *
from django.conf.urls.static import static
from vege.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    #base
    path('', include('myapp.urls')),
    path('contact/', contact, name = "contact"),
    path('about/', about, name="about"),
    path('index/', index, name="index"),
    path('success-page/', success_page, name="Success_page"),
    #vege app Urls
    path('receipes/', receipes, name="receipes"),
    path('delete-receipe/<id>/', delete_receipes, name="delete_receipes"),
    path('update-receipe/<id>/', update_receipe, name="update_receipe")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()    
"""DjangoWordCount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('', jobs.views.home),
    path('UploadPicture/', jobs.views.InputImageEntry, name="UploadPicture"),
    #path('InputImageEntry/', jobs.views.InputImageEntry, name="InputImageEntry"),
    path('home/', jobs.views.home, name="home"),
    path('aboutpage/', views.aboutpage, name="about"),
    path('WordCounterInput', views.WordCounterInput, name="WordCounterInput"),
    path('WordCounterOutput', views.WordCounterOutput, name="WordCounterOutput"),
    path('admin/', admin.site.urls, name="admin"),
    path('caption/', include('portfolio.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
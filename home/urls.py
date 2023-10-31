# home uygulamasındaki urls.py dosyası
from django.urls import path
from . import views

app_name = 'home'  # Bu, uygulama ad alanını ayarlar
urlpatterns = [
    path('', views.index, name='index'),
    # Diğer URL şemaları
]
# home uygulamasındaki views.py dosyası
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# Register your models here.
# home uygulamasındaki models.py dosyası
from django.db import models

# Create your models here.
# home uygulamasındaki apps.py dosyası

from django.apps import AppConfig


class HomeConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'home'
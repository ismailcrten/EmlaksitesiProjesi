# home uygulamasındaki urls.py dosyası
from django.urls import path
from . import views

app_name = 'home'  # Bu, uygulama ad alanını ayarlar
urlpatterns = [
    path('', views.index, name='index'),
    # Diğer URL şemaları
]


# Create your models here.
# home uygulamasındaki apps.py dosyası

from django.apps import AppConfig


class HomeConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'home'
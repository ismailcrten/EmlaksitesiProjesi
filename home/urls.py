# home uygulamasındaki urls.py dosyası
import home
from django.urls import path
from . import views

app_name = 'home'  # Bu, uygulama ad alanını ayarlar
urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),




    # Diğer URL şemaları
]


# Create your models here.
# home uygulamasındaki apps.py dosyası

from django.apps import AppConfig


class HomeConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'home'
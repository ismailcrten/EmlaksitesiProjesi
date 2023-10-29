# home uygulamasındaki urls.py dosyası
from django.urls import path
from . import views

app_name = 'home'  # Bu, uygulama ad alanını ayarlar
urlpatterns = [
    path('', views.index, name='index'),
    # Diğer URL şemaları
]

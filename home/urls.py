# home uygulamasındaki urls.py dosyası
import home
from django.urls import path


from . import views
from django.apps import AppConfig

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda/', views.hakkimizda),
    path('iletisim/', views.iletisim),

]


# Create your models here.
# home uygulamasındaki apps.py dosyası




class HomeConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'home'
from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:id>/<slug:slug>/', views.category_emlak, name='category_emlak'),
    # Diğer URL tanımları buraya eklenir
]

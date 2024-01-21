from django.urls import path
from renting.views import(
    homeView, apartDetailView, createApartView, 
    editApartView, deleteImage, panelView, approveView, 
    rejectView, user_profile, profile, favorite, addFavorite, removeFavorite, ilanlarim,
    deleteRenting, metaView, contactView, not_found, about
)

app_name = 'renting'

urlpatterns = [
    path('', homeView, name='home'),
    path('apart/<uuid:pk>', apartDetailView, name='apart'),
    path('create/', createApartView, name='create'),
    path('edit/<uuid:pk>/', editApartView, name='edit'),
    path('delete/<int:pk>/', deleteImage, name='delete'),
    path('panel/', panelView, name='panel'),
    path('approve/<uuid:pk>/', approveView, name='approve'),
    path('reject/<uuid:pk>/', rejectView, name='reject'),
    path('profile/', user_profile, name='user_profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('favorite/', favorite, name='favorite'),
    path('add_favorite/<uuid:pk>/', addFavorite, name='add_favorite'),
    path('remove_favorite/<uuid:pk>/', removeFavorite, name='remove_favorite'),
    path('ilanlarim/', ilanlarim, name='ilanlarim'),
    path('deleteRenting/<uuid:pk>/', deleteRenting, name='deleteRenting'),
    path('panel/meta/', metaView, name='meta'),
    path('contact/', contactView, name='contact'),
    path('notfound/', not_found, name='notfound'),
    path('about/', about, name='about'),
]
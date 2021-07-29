from django.urls import path
from .views import home

urlpatterns = [
    path('/Bienvenidos a DevGames con Criscrazy', home, name='Bienvenidos a DevGames con Criscrazy'),
]
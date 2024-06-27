from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_film, name='add_film'),
    path('films/', views.film_list, name='film_list'),
]

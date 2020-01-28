 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink_list, name='drink_list'),
    path('', views.recipe_list, name='recipe_list'),
]
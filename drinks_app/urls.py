 from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('drinks/', views.DrinkList.as_view(), name='drinks_list'),
    path('drinks/<int:pk>', views.DrinkDetail.as_view(), name='drinks_detail'),
]

# urlpatterns = [
#     path('', views.drink_list, name='drink_list'),
#     path('', views.recipe_list, name='recipe_list'),
# ]
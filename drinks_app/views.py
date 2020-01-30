from django.shortcuts import render
from .serializers import DrinkSerializer, RecipeSerializer 
from .models import Drink
from .models import Recipe
from rest_framework import generics 

class DrinkList(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DrinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# from .models import Drink, Recipe, Comment

# def drink_list(request):
#     drinks = Drink.objects.all()
#     return render(request, 'drinks_app/drink_list.html', {'drinks': drinks})

# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'drinks_app/recipe_list.html', {'recipes': recipes})    

    
                                                                                                                                                                                                                                 
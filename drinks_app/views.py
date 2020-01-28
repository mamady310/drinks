from django.shortcuts import render

from .models import Drink, Recipe, Comment

def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks_app/drink_list.html', {'drinks': drinks})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'drinks_app/recipe_list.html', {'recipes': recipes})    
                                                                                                                                                                                                                                 
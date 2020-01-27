from django.shortcuts import render

from .models import Drink

def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks_app/drink_list.html', {'drinks': drinks})

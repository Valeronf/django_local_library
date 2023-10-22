from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

# EXERCISE
# Our pizzas : Vegetarian : 8.55$, 4 cheeses : xx, Chicken mushrooms : xxx, Meat lover

def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_names_and_price = [pizza.name + " : " + str(pizza.price) + "$" for pizza in pizzas]
    pizzas_names_and_price_str = ", ".join(pizzas_names_and_price)
    return HttpResponse("Our pizzas : " + pizzas_names_and_price_str)'''
    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas': pizzas})
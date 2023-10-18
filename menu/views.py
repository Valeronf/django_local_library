from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.

def index(request):
    '''pizzas = Pizza.objects.all()
    pizza_names_and_price = [pizza.name + ': ' + str(pizza.price) + '€' for pizza in pizzas]
    pizza_names_str = ', '.join(pizza_names_and_price)
    return HttpResponse('Our pizzas : ' + pizza_names_str)'''
    pizzas = Pizza.objects.all().order_by("price")
    return render(request, 'menu/index.html', {'pizzas': pizzas})

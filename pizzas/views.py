from django.shortcuts import render, redirect

# Create your views here.

from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm

def index(request):
    """Strona główna"""
    return render(request, "pizzas/index.html")


def pizzas(request):
    """Strona z dostępnymi pizzami"""
    orderedPizza = Pizza.objects.order_by('name')
    context = {"orderedPizza": orderedPizza}
    return render(request, "pizzas/pizzas.html", context)


def toppings(request, pizza_id):
    """Wyświetla wybrane dodatki"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("pizza")
    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/toppings.html", context)


def edit_pizza(request, topping_id):
    """Edycja pizzy"""
    topping = topping.objects.get(id=topping_id)
    pizza = topping.pizza

    if request.method != 'POST':
        form = ToppingForm(instance=topping)
    else:
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.safe()
            return redirect("pizzas:toppings", pizza_id=pizza_id)

    context = {"topping": topping, "pizza": pizza, "form": form}
    return render(request, "pizzas/edit_toppings.html", context)

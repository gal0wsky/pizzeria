"""Definiuje wzorce adresów dla Pizzas."""

from django.urls import path
from . import views

app_name = "pizzas"
urlpatterns = [
    #Strona główna
    path("", views.index, name="index"),
    #Strona z dostępnymi pizzami
    path("pizzas/", views.pizzas, name="pizzas"),
    #Strona z wybranymi dodatkami
    path("pizzas/(<int:pizza_id>)/", views.toppings, name="toppings"),
    #Strona przeznaczona do edycji pizzy
    path("edit_toppings/(<int:topping_id>)/", views.edit_toppings, name="edit_toppings"),
]

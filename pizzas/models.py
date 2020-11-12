from django.db import models

# Create your models here.

class Pizza(models.Model):
    #name = ["hawajska", "miesna"]
    PIZZA_CHOICES = (('hawajska', "hawajska"), ('miesna', "miesna"))
    name = models.CharField(blank=True, choices=PIZZA_CHOICES, max_length=10)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    #toppings = ["ananas", "bekon", "sos"]
    TOPPINGS_CHOICES = (('ananas', "ananas"), ('bekon', "bekon"), ('sos', "sos"))
    toppings = models.CharField(blank=True, choices=TOPPINGS_CHOICES, max_length=10)

    def __str__(self):
        return self.toppings

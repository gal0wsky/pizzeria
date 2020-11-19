from django import forms
from .models import Pizza, Topping

# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ["text"]
#         labels = {"text": ""}


class ToppingForm(forms.ModelForm):
    choices = forms.ChoiceField(choices=Topping.TOPPINGS_CHOICES)
    class Meta:
        model = Topping
        fields = ["toppings", "choices"]
        labels = {"toppings": ""}
        # widgets = {"toppings": forms.ChoiceField(choices=Topping.TOPPINGS_CHOICES)}

from django import forms
from . import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["text"]
        labels = {"text": ""}


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}

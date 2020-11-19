from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Rejestracja nowego użytkownika"""
    if request.method != 'POST':
        #Wyświetlenie pustego formularza rejestracji
        form = UserCreationForm()
    else:
        #Przetworzenie danych
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.saev()
            #Zalogowanie użytkownika i przekierowanie na stronę główną
            login(request, new_user)
            return redirect("pizzas:index")

    #Wyświetlenie pustego formularza
    context = {"form": form}
    return render(request, "registration/register.html", context)

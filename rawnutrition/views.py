from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FoodItemFormSet, RegisterForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

#  Login or registration related views

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Log in the user
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


# Main Views

def index(request):

    # Example data
    user_targets = {
        'calories': 2000,
        'protein': 150,
        'carbs': 300,
        'fats': 70,
        'sat_fats': 25,
        'sugar': 50
    }

    user_consumption = {
        'calories': 1000,
        'protein': 75,
        'carbs': 150,
        'fats': 35,
        'sat_fats': 12,
        'sugar': 25
    }

    macro_percentages = {key: (
        value / user_targets[key] * 100) for key, value in user_consumption.items()}


    if request.method == 'POST':
        formset = FoodItemFormSet(request.POST)
        if 'submit_single' in request.POST:
            form_index = int(request.POST['submit_single'])
            form = formset[form_index]
            if form.is_valid():
                # Process the individual form
                # Save, update, or perform other actions
                pass
        else:
            if formset.is_valid():
                formset.save()
                # Redirect or perform other actions for the whole formset
    else:
        formset = FoodItemFormSet()

    return render(request, "index.html", {'formset': formset, 'macro_percentages': macro_percentages})

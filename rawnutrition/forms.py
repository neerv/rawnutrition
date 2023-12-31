from django import forms
from django.forms import formset_factory
from .models import FoodItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name','quantity']  # Include other fields as necessary


FoodItemFormSet = formset_factory(FoodItemForm, extra=1)

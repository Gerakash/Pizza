from django.contrib.auth.models import User

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['product','quantity','user','payment_type']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required'),

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



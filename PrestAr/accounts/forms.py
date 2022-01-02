from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Emprendedor
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class EmprendedorForm(forms.ModelForm):
#     class Meta:
#         model = Emprendedor
#         fields = ('apellido', 'nombre', 'dni')

class SignUpForm(UserCreationForm):
    class Meta:
        model = Emprendedor
        fields = ("username", "email")


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

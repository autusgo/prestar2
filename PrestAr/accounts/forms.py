from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Emprendedor
from django import forms


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']


class EmprendedorCreationForm(UserCreationForm):

    class Meta:
        model = Emprendedor
        fields = ('username', 'nombre', 'apellido',
                  'dni', 'celular', 'provincia', 'telefono')


class EmprendedorChangeForm(UserChangeForm):

    class Meta:
        model = Emprendedor
        fields = ('username', 'email', 'telefono')

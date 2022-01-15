from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Emprendedor


class EmprendedorCreationForm(Emprendedor):

    class Meta:
        model = Emprendedor
        fields = ('username', 'email')


class EmprendedorChangeForm(Emprendedor):

    class Meta:
        model = Emprendedor
        fields = ('username', 'email')

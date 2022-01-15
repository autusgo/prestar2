from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Emprendedor


class EmprendedorCreationForm(UserCreationForm):

    class Meta:
        model = Emprendedor
        fields = ('username', 'email')


class EmprendedorChangeForm(UserChangeForm):

    class Meta:
        model = Emprendedor
        fields = ('username', 'email')

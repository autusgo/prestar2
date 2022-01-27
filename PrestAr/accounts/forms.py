from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Emprendedor
from prestamos.models import Domicilio
from django import forms


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type = 'date'


class EmailInput(forms.EmailInput):
    input_type = 'email'


class EmprendedorCreationForm(UserCreationForm):
    class Meta:
        model = Emprendedor
        fields = ('username', 'nombre', 'apellido', 'genero', 'identidad', 'dni',
                  'fec_nac', 'estado_civil', 'telefono', 'celular', 'educacion', 'provincia')
        widgets = {
            'fec_nac': DateInput(),
            'username': EmailInput(),
        }


class EmprendedorChangeForm(UserChangeForm):

    class Meta:
        model = Emprendedor
        fields = ('username', 'email', 'telefono')


class DomicilioCreationForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ['calle', 'numero', 'piso', 'depto', 'monoblock', 'kilometro',
                  'barrio', 'manzana', 'seccion', 'casa', 'provincia', 'departamento', 'municipio', 'localidad', 'cod_postal', 'condicion']

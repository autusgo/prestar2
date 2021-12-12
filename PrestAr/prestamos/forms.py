from django import forms
from .models import *


class SimulacionForm(forms.ModelForm):
    class Meta:
        model = Simulacion
        fields = ['nom_ape', 'monto',
                  'cant_cuotas', 'tasa_anual']

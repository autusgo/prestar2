from django import forms
from .models import *


class SimulacionForm(forms.ModelForm):
    class Meta:
        model = Simulacion
        fields = ['apellido', 'nombre', 'telefono', 'email', 'monto',
                  'cant_cuotas', 'tasa_anual', 'dni']
        # initial = 3

    def __init__(self, *args, **kwargs):
        super(SimulacionForm, self).__init__(*args, **kwargs)
        self.fields['tasa_anual'].disabled = True
        self.fields['tasa_anual'].initial = 3

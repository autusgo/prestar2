from django import forms
from .models import *


class SimulacionForm(forms.ModelForm):
    class Meta:
        model = Simulacion
        fields = ['apellido', 'nombre', 'telefono', 'email', 'monto',
                  'cant_cuotas', 'tasa_anual', 'dni']
        # initial = 3

    # def __init__(self, *args, **kwargs):
    #     super(SimulacionForm, self).__init__(*args, **kwargs)
    #     self.fields['tasa_anual'].disabled = True
    #     self.fields['tasa_anual'].initial = 3


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['descripcion_emp', 'inicio_actividad', 'domicilio_emp', 'datos_contacto', 'personal_familiar', 'personal_nofamiliar',
                  'ingreso_emp_mes', 'gastos_emp', 'ingresos_familiares_mes', 'gastos_familiares_mes', 'notas', 'importe_solicitado', 'cant_cuotas', 'tasa_interes']

    # def __init__(self, *args, **kwargs):
    #     super(SolicitudForm, self).__init__(*args, **kwargs)


class SMVMForm(forms.ModelForm):
    class Meta:
        model = SMVM
        fields = ['monto']


class TasaInteresForm(forms.ModelForm):
    class Meta:
        model = TasaInteres
        fields = ['tasa']

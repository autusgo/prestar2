from django import forms
from .models import *
from prestamos.models import Emprendedor
from django.core.exceptions import ValidationError
from django.core import validators


class DateInput(forms.DateInput):
    input_type = 'date'


class SimulacionForm(forms.ModelForm):
    class Meta:
        model = Simulacion
        fields = ['apellido', 'nombre', 'telefono', 'email', 'importe_solicitado',
                  'cant_cuotas', 'tasa_anual', 'dni']
        # initial = 3

    # def __init__(self, *args, **kwargs):
    #     super(SimulacionForm, self).__init__(*args, **kwargs)
    #     self.fields['tasa_anual'].disabled = True
    #     self.fields['tasa_anual'].initial = 3


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['descripcion_emp', 'rubro', 'inicio_actividad', 'datos_contacto', 'personal_familiar', 'personal_nofamiliar',
                  'ingreso_emp_mes', 'gastos_emp', 'ingresos_familiares_mes', 'gastos_familiares_mes', 'notas', 'importe_solicitado', 'cant_cuotas', 'tasa_anual']
        widgets = {
            'inicio_actividad': DateInput(),
        }

# class EmprendedorForm(forms.ModelForm):
#     class Meta:
#         model = Emprendedor
#         fields = '__all__'


class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ['calle', 'numero', 'piso', 'depto', 'monoblock', 'kilometro',
                  'barrio', 'manzana', 'seccion', 'casa', 'provincia', 'departamento', 'municipio', 'localidad', 'cod_postal', 'condicion']


class SMVMForm(forms.ModelForm):
    class Meta:
        model = SMVM
        fields = ['monto']


class TasaInteresForm(forms.ModelForm):
    class Meta:
        model = TasaInteres
        fields = ['tasa']

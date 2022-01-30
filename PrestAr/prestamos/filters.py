from django.db.models.fields import DateField
import django_filters
from .models import Simulacion, Solicitud
from django_filters import FilterSet, CharFilter, DateFilter, NumberFilter
from django import forms
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class SimulacionFilter(django_filters.FilterSet):

    # def clean(self):
    #     cleaned_data = self(SimulacionFilter, self).clean()
    #     start_date = cleaned_data.get("start_date")
    #     end_date = cleaned_data.get("end_date")

    #     if start_date > end_date:
    #         self._errors['start_date'] = self._errors.get('start_date', [])
    #         self._errors['start_date'].append(
    #             "Start date must be before end date.")

    #     return cleaned_data

    apellido = CharFilter(field_name="apellido", lookup_expr='icontains')
    dni = NumberFilter(field_name="dni")
    start_date = DateFilter(field_name="created_date",
                            lookup_expr='date__gte', widget=DateInput)
    end_date = DateFilter(field_name="created_date",
                          lookup_expr='date__lte', widget=DateInput)
    monto_desde = NumberFilter(
        field_name="importe_solicitado", lookup_expr='gte')
    monto_hasta = NumberFilter(
        field_name="importe_solicitado", lookup_expr='lte')

    class Meta:
        model = Simulacion
        fields = '__all__'


class SolicitudFilter(django_filters.FilterSet):
    apellido = CharFilter(field_name="apellido", lookup_expr='icontains')
    dni = NumberFilter(field_name="dni")
    start_date = DateFilter(field_name="created_date",
                            lookup_expr='date__gte', widget=DateInput)
    end_date = DateFilter(field_name="created_date",
                          lookup_expr='date__lte', widget=DateInput)
    monto_desde = NumberFilter(
        field_name="importe_solicitado", lookup_expr='gte')
    monto_hasta = NumberFilter(
        field_name="importe_solicitado", lookup_expr='lte')

    class Meta:
        model = Solicitud
        fields = '__all__'

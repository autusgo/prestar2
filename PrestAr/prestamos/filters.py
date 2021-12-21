from django.db.models.fields import DateField
import django_filters
from .models import Simulacion
from django_filters import FilterSet, CharFilter, DateFilter, NumberFilter
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class SimulacionFilter(django_filters.FilterSet):
    nom_ape = CharFilter(field_name="nom_ape", lookup_expr='icontains')
    start_date = DateFilter(field_name="created_date",
                            lookup_expr='gte', widget=DateInput)
    end_date = DateFilter(field_name="created_date",
                          lookup_expr='lte', widget=DateInput)
    monto_desde = NumberFilter(field_name="monto", lookup_expr='gte')
    monto_hasta = NumberFilter(field_name="monto", lookup_expr='lte')

    class Meta:
        model = Simulacion
        fields = '__all__'

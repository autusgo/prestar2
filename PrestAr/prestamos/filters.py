import django_filters
from .models import Simulacion
from django_filters import FilterSet, CharFilter


class SimulacionFilter(django_filters.FilterSet):
    nom_ape = CharFilter(field_name="nom_ape", lookup_expr='icontains')
    created_date = CharFilter(
        field_name="created_date", lookup_expr='icontains')

    class Meta:
        model = Simulacion
        fields = ['nom_ape', 'created_date', 'email']

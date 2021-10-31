import django_filters
from .models import Simulacion
from django_filters import FilterSet


class SimulacionFilter(django_filters.FilterSet):
    class Meta:
        model = Simulacion
        fields = ['nom_ape']

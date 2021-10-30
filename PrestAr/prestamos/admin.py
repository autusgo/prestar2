from django.contrib import admin
from .models import *


class SimulacionAdmin(admin.ModelAdmin):
    list_display = ['nom_ape', 'created_date', 'calculo_cuota']


admin.site.register(Simulacion, SimulacionAdmin)

from django.contrib import admin
from .models import *


class SimulacionAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'created_date', 'dni', 'calculo_cuota']


admin.site.register(Simulacion, SimulacionAdmin)

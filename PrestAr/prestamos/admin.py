from django.contrib import admin
from .models import *


class SimulacionAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'created_date', 'dni', 'calculo_cuota']


admin.site.register(Simulacion, SimulacionAdmin)


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(Solicitud, SolicitudAdmin)


class TasaInteresAdmin(admin.ModelAdmin):
    list_display = ['tasa', 'created_date', 'author']


admin.site.register(TasaInteres, TasaInteresAdmin)


class SMVMAdmin(admin.ModelAdmin):
    list_display = ['monto', 'created_date', 'author']


admin.site.register(SMVM, SMVMAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmprendedorCreationForm, EmprendedorChangeForm
from .models import Emprendedor


class EmprendedorAdmin(UserAdmin):
    add_form = EmprendedorCreationForm
    form = EmprendedorChangeForm
    model = Emprendedor
    list_display = ['email', 'username', ]


admin.site.register(Emprendedor, EmprendedorAdmin)

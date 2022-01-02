from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Emprendedor


class CustomUserAdmin(UserAdmin):
    model = Emprendedor
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']


admin.site.register(Emprendedor, CustomUserAdmin)

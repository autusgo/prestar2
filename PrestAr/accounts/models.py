from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
# Create your models here.


# class Emprendedor(AbstractUser):
#     pass
#     # add additional fields in here

#     def __str__(self):
#         return self.username


class Emprendedor(AbstractUser):
    GENEROS_LISTA = [
        ('femenino', 'Femenino'),
        ('masculino', 'Masculino'),
        ('otre', 'Otre'),
    ]
    IDENTIDAD_LISTA = [
        ('mujercis', 'Mujer'),
        ('hombrecis', 'Hombre'),
        ('mujertrans', 'Mujer trans'),
        ('hombretrans', 'Hombre trans'),
        ('nobinarie', 'No binarie'),
        ('nodeclara', 'Prefiero no decir'),
    ]
    ESTADO_CIVIL = [
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Dovorciado'),
        ('viudo', 'Viudo'),
        ('concubinato', 'Concubinato'),
        ('unioncivil', 'Unión civil'),
    ]
    NIVEL_EDUCATIVO = [
        ('prim_inc', 'Primario incompleto'),
        ('prim_comp', 'Primario completo'),
        ('sec_inc', 'Secundario incompleto'),
        ('sec_comp', 'Secundario completo'),
        ('terc_inc', 'Terciario incompleto'),
        ('terc_comp', 'Terciario completo'),
        ('uni_inc', 'Universitario incompleto'),
        ('uni_comp', 'Universitario completo'),
    ]

    nombre = models.CharField(max_length=200, null=True)
    apellido = models.CharField(max_length=200, null=True)
    genero = models.CharField(max_length=200, choices=GENEROS_LISTA)
    identidad = models.CharField(
        max_length=200, choices=IDENTIDAD_LISTA, blank=True, null=True)
    dni = models.IntegerField(null=True)
    fec_nac = models.DateField(null=True)
    estado_civil = models.CharField(
        max_length=200, choices=ESTADO_CIVIL, null=True)
    telefono = models.IntegerField(null=True)
    celular = models.BooleanField(default=True)
    email = models.CharField(max_length=200, null=True)
    educacion = models.CharField(
        max_length=200, choices=NIVEL_EDUCATIVO, null=True)
    provincia = models.CharField(max_length=20)

    def __str__(self):
        return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from datetime import date
# Create your models here.


# class Emprendedor(AbstractUser):
#     pass
#     # add additional fields in here

#     def __str__(self):
#         return self.username


class Emprendedor(AbstractUser):
    GENEROS_LISTA = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('X', 'Otre'),
    ]
    IDENTIDAD_LISTA = [
        ('Mujer cis', 'Mujer'),
        ('Hombre cis', 'Hombre'),
        ('Mujer trans', 'Mujer trans'),
        ('Hombre trans', 'Hombre trans'),
        ('No binarie', 'No binarie'),
        ('No declara', 'Prefiero no decir'),
    ]
    ESTADO_CIVIL = [
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Dovorciado'),
        ('Viudo', 'Viudo'),
        ('Concubinato', 'Concubinato'),
        ('Unión Civil', 'Unión civil'),
    ]
    NIVEL_EDUCATIVO = [
        ('Primario incompleto', 'Primario incompleto'),
        ('Primario Completo', 'Primario completo'),
        ('Primario completo', 'Secundario incompleto'),
        ('Secundario completo', 'Secundario completo'),
        ('Terciario incompleto', 'Terciario incompleto'),
        ('Terciario completo', 'Terciario completo'),
        ('Universitario incompleto', 'Universitario incompleto'),
        ('Universitario completo', 'Universitario completo'),
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
    domicilio = models.ForeignKey(
        "prestamos.Domicilio", on_delete=models.CASCADE)

    def age(self):
        age = int((date.today() - self.fec_nac).days / 365.25)
        return age

    # def menor(self):
    #     if self.age > 17:
    #         return True
    #     else:
    #         return False

    def __str__(self):
        return self.username

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
    PROVINCIAS_LISTA = [
        ('buenosaires', 'Buenos Aires'),
        ('caba', 'Ciudad Autónoma de Buenos Aires'),
        ('catamarca', 'Catamarca'),
        ('chaco', 'Chaco'),
        ('chubut', 'Chubut'),
        ('cordoba', 'Córdoba'),
        ('honeydew', 'Honeydews'),
        ('corrientes', 'Corrientes'),
        ('entrerios', 'Entre Ríos'),
        ('formosa', 'Formosa'),
        ('jujuy', 'Jujuy'),
        ('lapampa', 'La Pampa'),
        ('larioja', 'La Rioja'),
        ('mendoza', 'Mendoza'),
        ('misiones', 'Misiones'),
        ('neuquen', 'Neuquén'),
        ('rionegro', 'Río Negro'),
        ('salta', 'Salta'),
        ('sanjuan', 'San Juan'),
        ('sanluis', 'San Luis'),
        ('santacruz', 'Santa Cruz'),
        ('santafe', 'Santa Fe'),
        ('santiagoestero', 'Santiago del Estero'),
        ('tierafuego', 'Tierra del Fuego'),
        ('tucuman', 'Tucumán'),
    ]

    nombre = models.CharField(max_length=200, null=True)
    apellido = models.CharField(max_length=200, null=True)
    dni = models.IntegerField(null=True)
    telefono = models.IntegerField(null=True)
    celular = models.BooleanField(null=True, default=True)
    email = models.CharField(max_length=200, null=True)

    provincia = models.CharField(
        max_length=200, choices=PROVINCIAS_LISTA)

    def __str__(self):
        return self.username


# class Customer(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.name


# class Tag(models.Model):
#     name = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     CATEGORY = (
#         ('Indoor', 'Indoor'),
#         ('Out Door', 'Out Door'),
#     )

#     name = models.CharField(max_length=200, null=True)
#     price = models.FloatField(null=True)
#     category = models.CharField(max_length=200, null=True, choices=CATEGORY)
#     description = models.CharField(max_length=200, null=True, blank=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     tags = models.ManyToManyField(Tag)

#     def __str__(self):
#         return self.name


# class Order(models.Model):
#     STATUS = (
#         ('Pending', 'Pending'),
#         ('Out for delivery', 'Out for delivery'),
#         ('Delivered', 'Delivered'),
#     )

#     customer = models.ForeignKey(
#         Customer, null=True, on_delete=models.SET_NULL)
#     product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     status = models.CharField(max_length=200, null=True, choices=STATUS)
#     note = models.CharField(max_length=1000, null=True)

#     def __str__(self):
#         return self.product.name

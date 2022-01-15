from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.db.models.deletion import CASCADE
# from django.contrib.auth.base_user import BaseUserManager

# Create your models here.


# class Domicilio(models.Model):
#     calle = models.CharField(max_length=200)
#     numero = models.CharField(max_length=9)
#     ciudad = models.CharField(max_length=200)
#     cod_pot = models.IntegerField()
#     provincia = models.CharField(max_length=200)

#     def __str__(self):
#         return self.calle


class Emprendedor(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

# class Emprendedor(AbstractUser):
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('user',)
#     user = models.OneToOneField(
#         User, related_name='emprendedor', unique=True, on_delete=CASCADE)
#     nombre = models.CharField(max_length=200)
#     apellido = models.CharField(max_length=200)
#     dni = models.IntegerField()
#     fecha_nac = models.DateField(blank=True, null=True)
#     telefono = models.IntegerField()
#     celular = models.BooleanField()
#     email = models.CharField(max_length=200)
#     domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

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

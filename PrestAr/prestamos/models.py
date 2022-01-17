from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


class Simulacion(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField(validators=[
                              MaxValueValidator(99999999)])
    monto = models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)
    tasa_anual = models.SmallIntegerField()
    cant_cuotas = models.SmallIntegerField()
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def publish(self):
        self.created_date = timezone.now()
        self.author = request.user.is_authenticated
        self.save()

    def calculo_cuota(self):
        calculo_cuota = round(self.monto*(0.03/12) /
                              (1-(1+(0.03/12))**(-self.cant_cuotas)), 2)
        return round(calculo_cuota, 2)

    def __unicode__(self):
        return '{} {} {}'.format(self.apellido, self.dni, self.created_date)

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Max
from accounts.models import Emprendedor
from datetime import date


class SMVM(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    monto = models. PositiveIntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.author = request.user.is_authenticated
        self.save()

    def __str__(self):
        return '{}'.format(self.monto)

    def __unicode__(self):
        return '{}'.format(self.monto)


class TasaInteres(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tasa = models.PositiveIntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.author = request.user.is_authenticated
        self.save()

    def __str__(self):
        return '{}'.format(self.tasa)

    def __unicode__(self):
        return '{}'.format(self.tasa)


class Simulacion(models.Model):
    smvm = models.ForeignKey(
        SMVM, on_delete=models.CASCADE, null=True, default=1)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)  # Acá tiene que quedar el null=True porque se tiene que poder hacer simulaciones sin registrarse
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField(validators=[
                              MaxValueValidator(99999999)])
    importe_solicitado = models.PositiveIntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)
    tasa_anual = models.ForeignKey(
        TasaInteres, on_delete=models.CASCADE, null=True, default=1)
    cant_cuotas = models.SmallIntegerField()
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cuota_final = models.DecimalField(
        decimal_places=2, max_digits=9, null=True)

    def publish(self):
        self.created_date = timezone.now()
        self.author = request.user.is_authenticated
        self.save()

    def calculo_cuota(self):
        interes = int(self.tasa_anual.tasa)/100
        calculo_cuota = round(self.importe_solicitado*(interes/12) /
                              (1-(1+(interes/12))**(-self.cant_cuotas)), 2)
        return round(calculo_cuota, 2)

    def save(self, *args, **kwargs):
        # Toma el resultado de la función y lo guarda en el modelo
        self.cuota_final = self.calculo_cuota()
        super(Simulacion, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} {} {}'.format(self.apellido, self.dni, self.created_date)


class Domicilio(models.Model):
    PROVINCIAS_LISTA = [
        ('Buenos Aires', 'Buenos Aires'),
        ('CABA', 'CABA'),
        ('Catamarca', 'Catamarca'),
        ('Chaco', 'Chaco'),
        ('Chubut', 'Chubut'),
        ('Córdoba', 'Córdoba'),
        ('Corrientes', 'Corrientes'),
        ('Entre Ríos', 'Entre Ríos'),
        ('Formosa', 'Formosa'),
        ('Jujuy', 'Jujuy'),
        ('La Pampa', 'La Pampa'),
        ('La Rioja', 'La Rioja'),
        ('Mendoza', 'Mendoza'),
        ('Misiones', 'Misiones'),
        ('Neuquén', 'Neuquén'),
        ('Río Negro', 'Río Negro'),
        ('Salta', 'Salta'),
        ('San Juan', 'San Juan'),
        ('San Luis', 'San Luis'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Santa Fe', 'Santa Fe'),
        ('Santiago del Estero', 'Santiago del Estero'),
        ('Tierra del Fuego', 'Tierra del Fuego'),
        ('Tucumán', 'Tucumán'),
    ]
    CONDICION_LISTA = [
        ('Propio', 'Propio'),
        ('Alquilado', 'Alquilado'),
        ('Prestado', 'Prestado'),
        ('Leasing', 'Leasing'),
        ('Otro', 'Otro'),
    ]

    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    piso = models.CharField(max_length=20, blank=True)
    depto = models.CharField(max_length=20, blank=True)
    monoblock = models.CharField(max_length=20, blank=True)
    kilometro = models.CharField(max_length=20, blank=True)
    barrio = models.CharField(max_length=200, blank=True)
    manzana = models.CharField(max_length=20, blank=True)
    seccion = models.CharField(max_length=20, blank=True)
    casa = models.CharField(max_length=20, blank=True)
    provincia = models.CharField(
        max_length=200, choices=PROVINCIAS_LISTA, null=True)
    departamento = models.CharField(max_length=200, blank=True)
    municipio = models.CharField(max_length=200, blank=True)
    localidad = models.CharField(max_length=200, blank=True)
    cod_postal = models.CharField(max_length=20, blank=True)
    condicion = models.CharField(max_length=200, choices=CONDICION_LISTA)

    def __str__(self):
        return '{} {}'.format(self.calle, self.numero)

    def __unicode__(self):
        return '{} {}'.format(self.calle, self.numero)

#   SOLICITUDES


class Solicitud(models.Model):

    RUBRO_LISTA = [
        ('Producción', 'Producción'),
        ('Comercialización', 'Comercialización'),
        ('Servicios', 'Servicios'),
    ]

    smvm = models.ForeignKey(
        SMVM, on_delete=models.CASCADE, null=True, default=1)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emprendedor = models.ForeignKey(
        Emprendedor, on_delete=models.CASCADE, related_name='emprendedor')
    created_date = models.DateTimeField(
        default=timezone.now, null=True)
    descripcion_emp = models.TextField()
    rubro = models.CharField(max_length=200, choices=RUBRO_LISTA)
    inicio_actividad = models.DateField()
    domicilio_viv = models.ForeignKey(
        Domicilio, on_delete=models.CASCADE, related_name='domicilioviv', null=True)
    domicilio_emp = models.ForeignKey(
        Domicilio, on_delete=models.CASCADE, related_name='domicilioemp')
    datos_contacto = models.IntegerField(blank=True)
    personal_familiar = models.IntegerField()
    personal_nofamiliar = models.IntegerField()
    ingreso_emp_mes = models.IntegerField()
    gastos_emp = models.IntegerField()
    resultado_emp = models.IntegerField(null=True)
    ingresos_familiares_mes = models.IntegerField(null=True, blank=True)
    gastos_familiares_mes = models.IntegerField(null=True, blank=True)
    resultado_familiar = models.IntegerField(null=True)
    resultado_total = models.IntegerField(null=True)
    notas = models.TextField(blank=True)
    importe_solicitado = models.PositiveIntegerField()
    cant_cuotas = models.IntegerField()
    tasa_anual = models.ForeignKey(
        TasaInteres, on_delete=models.CASCADE, null=True, default=1)
    destino1_texto = models.CharField(max_length=50, null=True)
    destino1_monto = models.IntegerField(null=True)
    destino2_texto = models.CharField(max_length=50, null=True)
    destino2_monto = models.IntegerField(null=True)
    destino3_texto = models.CharField(max_length=50, null=True)
    destino3_monto = models.IntegerField(null=True)
    cuota_final = models.DecimalField(
        decimal_places=2, max_digits=9, null=True)

    def publish(self):
        self.created_date = timezone.now()
        self.author = request.user.is_authenticated
        self.save()

    def calculo_cuota(self):
        interes = int(self.tasa_anual.tasa)/100
        calculo_cuota = round(self.importe_solicitado*(interes/12) /
                              (1-(1+(interes/12))**(-self.cant_cuotas)), 2)
        return round(calculo_cuota, 2)

    def minimo(self):
        minimo = float((date.today() - self.inicio_actividad).days / 365.25)
        if minimo > 0.5:
            minimo = True
        else:
            minimo = False
        return minimo

    def save(self, *args, **kwargs):
        # Toma el resultado de la función y lo guarda en el modelo
        self.cuota_final = self.calculo_cuota()
        super(Solicitud, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{}'.format(self.id)

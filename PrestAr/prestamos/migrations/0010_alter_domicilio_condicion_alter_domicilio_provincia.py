# Generated by Django 4.0.1 on 2022-01-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0009_alter_solicitud_emprendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domicilio',
            name='condicion',
            field=models.CharField(choices=[('Propio', 'Propio'), ('Alquilado', 'Alquilado'), ('Prestado', 'Prestado'), ('Leasing', 'Leasing'), ('Otro', 'Otro')], max_length=200),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='provincia',
            field=models.CharField(choices=[('Buenos Aires', 'Buenos Aires'), ('Ciudad Autónoma de Buenos Aires', 'Ciudad Autónoma de Buenos Aires'), ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'), ('Córdoba', 'Córdoba'), ('Honeydews', 'Honeydews'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'), ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'), ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'), ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'), ('San Juan', 'San Juan'), ('San Luis', 'San Luis'), ('Santa Cruz', 'Santa Cruz'), ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'), ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán')], max_length=200, null=True),
        ),
    ]
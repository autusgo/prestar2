# Generated by Django 4.0.1 on 2022-01-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0005_alter_domicilio_provincia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='gastos_familiares_mes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='ingresos_familiares_mes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
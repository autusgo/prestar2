# Generated by Django 4.0.1 on 2022-01-22 01:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0006_alter_solicitud_domicilio_viv'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]

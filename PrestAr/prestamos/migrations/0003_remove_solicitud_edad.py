# Generated by Django 4.0.1 on 2022-02-07 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0002_solicitud_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='edad',
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-23 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0011_alter_solicitud_domicilio_viv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='domicilio_viv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domicilioviv', to='prestamos.domicilio'),
        ),
    ]

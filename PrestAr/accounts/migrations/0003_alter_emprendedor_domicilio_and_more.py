# Generated by Django 4.0.1 on 2022-01-29 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0003_alter_solicitud_domicilio_emp'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprendedor',
            name='domicilio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prestamos.domicilio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='estado_civil',
            field=models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viudo', 'Viudo'), ('Concubinato', 'Concubinato'), ('Unión Civil', 'Unión civil')], max_length=200, null=True),
        ),
    ]

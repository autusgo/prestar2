# Generated by Django 4.0.1 on 2022-01-25 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0020_rename_monto_simulacion_importe_solicitado_and_more'),
        ('accounts', '0004_remove_emprendedor_domicilio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprendedor',
            name='domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prestamos.domicilio'),
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='educacion',
            field=models.CharField(choices=[('Primario incompleto', 'Primario incompleto'), ('prim_comp', 'Primario completo'), ('Primario completo', 'Secundario incompleto'), ('Secundario completo', 'Secundario completo'), ('Terciario incompleto', 'Terciario incompleto'), ('Terciario completo', 'Terciario completo'), ('Universitario incompleto', 'Universitario incompleto'), ('Universitario completo', 'Universitario completo')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='estado_civil',
            field=models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Divorciado', 'Dovorciado'), ('Viudo', 'Viudo'), ('Concubinato', 'Concubinato'), ('Unión Civil', 'Unión civil')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='genero',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('X', 'Otre')], max_length=200),
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='identidad',
            field=models.CharField(blank=True, choices=[('Mujer cis', 'Mujer'), ('Hombre cis', 'Hombre'), ('Mujer trans', 'Mujer trans'), ('Hombre trans', 'Hombre trans'), ('No binarie', 'No binarie'), ('No declara', 'Prefiero no decir')], max_length=200, null=True),
        ),
    ]
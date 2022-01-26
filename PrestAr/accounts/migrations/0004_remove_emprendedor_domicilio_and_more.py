# Generated by Django 4.0.1 on 2022-01-25 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_emprendedor_domicilio_alter_emprendedor_educacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprendedor',
            name='domicilio',
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='educacion',
            field=models.CharField(choices=[('prim_inc', 'Primario incompleto'), ('prim_comp', 'Primario completo'), ('sec_inc', 'Secundario incompleto'), ('sec_comp', 'Secundario completo'), ('terc_inc', 'Terciario incompleto'), ('terc_comp', 'Terciario completo'), ('uni_inc', 'Universitario incompleto'), ('uni_comp', 'Universitario completo')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='estado_civil',
            field=models.CharField(choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('divorciado', 'Dovorciado'), ('viudo', 'Viudo'), ('concubinato', 'Concubinato'), ('unioncivil', 'Unión civil')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='genero',
            field=models.CharField(choices=[('femenino', 'Femenino'), ('masculino', 'Masculino'), ('otre', 'Otre')], max_length=200),
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='identidad',
            field=models.CharField(blank=True, choices=[('mujercis', 'Mujer'), ('hombrecis', 'Hombre'), ('mujertrans', 'Mujer trans'), ('hombretrans', 'Hombre trans'), ('nobinarie', 'No binarie'), ('nodeclara', 'Prefiero no decir')], max_length=200, null=True),
        ),
    ]
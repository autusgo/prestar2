# Generated by Django 4.0.1 on 2022-01-18 01:21

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('apellido', models.CharField(max_length=200, null=True)),
                ('genero', models.CharField(choices=[('femenino', 'Femenino'), ('masculino', 'Masculino'), ('otre', 'Otre')], max_length=200, null=True)),
                ('identidad', models.CharField(choices=[('mujercis', 'Mujer'), ('hombrecis', 'Hombre'), ('mujertrans', 'Mujer trans'), ('hombretrans', 'Hombre trans'), ('nobinarie', 'No binarie'), ('nodeclara', 'Prefiero no decir')], max_length=200, null=True)),
                ('dni', models.IntegerField(null=True)),
                ('fec_nac', models.DateField(null=True)),
                ('estado_civil', models.CharField(choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('divorciado', 'Dovorciado'), ('viudo', 'Viudo'), ('concubinato', 'Concubinato'), ('unioncivil', 'Unión civil')], max_length=200, null=True)),
                ('telefono', models.IntegerField(null=True)),
                ('celular', models.BooleanField(default=True, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('educacion', models.CharField(choices=[('prim_inc', 'Primario incompleto'), ('prim_comp', 'Primario completo'), ('sec_inc', 'Secundario incompleto'), ('sec_comp', 'Secundario completo'), ('terc_inc', 'Terciario incompleto'), ('terc_comp', 'Terciario completo'), ('uni_inc', 'Universitario incompleto'), ('uni_comp', 'Universitario completo')], max_length=200, null=True)),
                ('provincia', models.CharField(choices=[('buenosaires', 'Buenos Aires'), ('caba', 'Ciudad Autónoma de Buenos Aires'), ('catamarca', 'Catamarca'), ('chaco', 'Chaco'), ('chubut', 'Chubut'), ('cordoba', 'Córdoba'), ('honeydew', 'Honeydews'), ('corrientes', 'Corrientes'), ('entrerios', 'Entre Ríos'), ('formosa', 'Formosa'), ('jujuy', 'Jujuy'), ('lapampa', 'La Pampa'), ('larioja', 'La Rioja'), ('mendoza', 'Mendoza'), ('misiones', 'Misiones'), ('neuquen', 'Neuquén'), ('rionegro', 'Río Negro'), ('salta', 'Salta'), ('sanjuan', 'San Juan'), ('sanluis', 'San Luis'), ('santacruz', 'Santa Cruz'), ('santafe', 'Santa Fe'), ('santiagoestero', 'Santiago del Estero'), ('tierafuego', 'Tierra del Fuego'), ('tucuman', 'Tucumán')], max_length=200, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

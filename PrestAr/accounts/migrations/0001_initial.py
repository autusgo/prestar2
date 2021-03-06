# Generated by Django 4.0.1 on 2022-02-07 04:21

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('X', 'Otre')], max_length=200)),
                ('identidad', models.CharField(blank=True, choices=[('Mujer cis', 'Mujer'), ('Hombre cis', 'Hombre'), ('Mujer trans', 'Mujer trans'), ('Hombre trans', 'Hombre trans'), ('No binarie', 'No binarie'), ('No declara', 'Prefiero no decir')], max_length=200, null=True)),
                ('dni', models.IntegerField(null=True)),
                ('fec_nac', models.DateField(null=True)),
                ('estado_civil', models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Divorciado', 'Dovorciado'), ('Viudo', 'Viudo'), ('Concubinato', 'Concubinato'), ('Uni??n Civil', 'Uni??n civil')], max_length=200, null=True)),
                ('telefono', models.IntegerField(null=True)),
                ('celular', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('educacion', models.CharField(choices=[('Primario incompleto', 'Primario incompleto'), ('Primario Completo', 'Primario completo'), ('Primario completo', 'Secundario incompleto'), ('Secundario completo', 'Secundario completo'), ('Terciario incompleto', 'Terciario incompleto'), ('Terciario completo', 'Terciario completo'), ('Universitario incompleto', 'Universitario incompleto'), ('Universitario completo', 'Universitario completo')], max_length=200, null=True)),
                ('provincia', models.CharField(max_length=20)),
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

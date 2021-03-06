# Generated by Django 4.0.4 on 2022-06-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista_nomina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cc', models.IntegerField()),
                ('salario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registro_mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('raza', models.CharField(max_length=40)),
                ('propietario', models.CharField(max_length=40)),
            ],
        ),
    ]

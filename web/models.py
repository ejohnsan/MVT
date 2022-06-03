import email
from django.db import models
from django.forms import CharField, IntegerField


# Create your models here.


class Lista_nomina(models.Model):

    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cc = models.IntegerField()
    salario = models.IntegerField()


class Registro_mascota(models.Model):

    nombre_mascota = models.CharField(max_length=40)
    edad = models.IntegerField()
    raza = models.CharField(max_length=40)
    propietario = models.CharField(max_length=40)



class Mensaje(models.Model):

    asunto = models.CharField(max_length=60)
    email = models.EmailField()
    mensaje = models.CharField(max_length=100)
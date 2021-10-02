from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    ocupacion = models.CharField('Ocupacion', max_length = 40)#, unique=True)
    nombre = models.CharField('Nombre', max_length = 45)
    edad = models.IntegerField()
    resguardo = models.CharField('Resguardo_o_Ciudad', max_length = 45)
    etnia = models.CharField('Etnia', max_length = 45)
    departamento = models.CharField('Departamento_Residencia', max_length = 45)
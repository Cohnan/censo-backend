from django.db import models

class Etnia(models.Model):
    id_etnia = models.BigAutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length = 40)
    descripcion= models.CharField('Descripcion', max_length = 1000)
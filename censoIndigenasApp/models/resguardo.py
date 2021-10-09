from django.db import models

class Resguardo(models.Model):
    id_resguardo = models.BigAutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length = 45)
    descripcion= models.CharField('Descripcion', max_length = 60)
    
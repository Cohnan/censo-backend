from django.db import models

class Etnia(models.Model):
    id_Etnia = models.BigAutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length = 40)
    descripcion= models.CharField('Descripcion', max_length = 60)
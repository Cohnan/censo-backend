from django.db import models
from censoIndigenasApp.models.etnia import Etnia
from censoIndigenasApp.models.ocupacion import Ocupacion

from censoIndigenasApp.models.resguardo import Resguardo


class Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_doc = models.CharField(max_length = 4)
    doc_id = models.IntegerField(null = True)
    id_ocupacion = models.ForeignKey(Ocupacion, related_name='ocupacion',on_delete= models.CASCADE)
    nombre = models.CharField('Nombre', max_length = 45)
    fechadenaciemiento = models.DateField()
    id_resguardo = models.ForeignKey(Resguardo, related_name='resguardo',on_delete= models.CASCADE)
    id_etnia = models.ForeignKey(Etnia, related_name='etnia',on_delete= models.CASCADE)
    departamento = models.CharField('Departamento_Residencia', max_length = 45)
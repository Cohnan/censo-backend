from django.db import models
from censoIndigenasApp.models.etnia import Etnia
from censoIndigenasApp.models.ocupacion import Ocupacion
from censoIndigenasApp.models.resguardo import Resguardo


class Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_doc = models.CharField("Tipo de documento", max_length = 4)
    doc_id = models.IntegerField("Número de documento", null = True)
    id_ocupacion = models.ForeignKey(Ocupacion, related_name='Ocupación',on_delete= models.CASCADE)
    nombre = models.CharField('Nombre', max_length = 45)
    fechadenacimiento = models.DateField("Fecha de Nacimiento")
    id_resguardo = models.ForeignKey(Resguardo, related_name='Resguardo',on_delete= models.CASCADE)
    id_etnia = models.ForeignKey(Etnia, related_name='Etnia',on_delete= models.CASCADE)
    departamento = models.CharField('Departamento de Residencia', max_length = 45)
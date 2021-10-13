from rest_framework import serializers;
from ..models import Etnia

class EtniaSerializer(serializers.ModelSerializer):
    # Los unicos campos que puede recibir el serializador para crear una instancia del modelo
    class Meta:
        model = Etnia
        fields = ("id_Etnia", "nombre", "descripcion")
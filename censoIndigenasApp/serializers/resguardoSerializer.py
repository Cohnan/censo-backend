from rest_framework import serializers;
from ..models import Resguardo

class ResguardoSerializer(serializers.ModelSerializer):
    # Los unicos campos que puede recibir el serializador para crear una instancia del modelo
    class Meta:
        model = Resguardo
        fields = ("id_resguardo", "nombre", "descripcion")
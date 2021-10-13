from rest_framework import serializers;
from ..models import Ocupacion

class OcupacionSerializer(serializers.ModelSerializer):
    # Los unicos campos que puede recibir el serializador para crear una instancia del modelo
    class Meta:
        model = Ocupacion
        fields = ["nombre", "descripcion"]
from rest_framework import serializers
<<<<<<< HEAD
=======

>>>>>>> d66dd5aa77c010a44f8480231455925faad290b4
from ..models       import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ["id" , "tipo_doc" , "doc_id" , "id_ocupacion" , "nombre" , "fechadenacimiento" , "id_resguardo" , "id_etnia" , "departamento"]

    def create(self, validated_data):
        personaInstance = Persona.objects.create(**validated_data)
        return personaInstance    

    def to_representation(self, obj):
        persona   = Persona.objects.get(id=obj.id)
        return {
            "id"               : persona.id,
            "tipo_doc"         : persona.tipo_doc,
            "doc_id"           : persona.doc_id,
            "id_ocupacion"     : persona.id_ocupacion,
            "nombre"           : persona.nombre,
            "fechadenacimiento": persona.fechadenacimiento,
            "id_resguardo"     : persona.id_resguardo,
            "id_etnia"         : persona.id_etnia,
            "departamento"     : persona.departamento
        }
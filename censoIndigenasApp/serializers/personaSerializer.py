from rest_framework import serializers

from ..models       import Persona, Ocupacion, Etnia, Resguardo


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ["id" , "tipo_doc" , "doc_id" , "id_ocupacion" , "nombre" , "fechadenacimiento" , "id_resguardo" , "id_etnia" , "departamento"]

    def create(self, validated_data):
        personaInstance = Persona.objects.create(**validated_data)
        return personaInstance    

    def to_representation(self, obj):
        persona   = Persona.objects.get(id=obj.id)
        ocupacion = obj.id_ocupacion    # Es una instancia del tipo Ocupacion
        etnia = obj.id_etnia            # Instancia del tipo Etnia
        resguardo = obj.id_resguardo    #Instancia del tipo Resguardo

        return {
            "id"                : persona.id,
            "tipo_doc"          : persona.tipo_doc,
            "doc_id"            : persona.doc_id,
            "nombre"            : persona.nombre,
            "fechadenacimiento" : persona.fechadenacimiento,
            "ocupacion"         : ocupacion.nombre,
            "etnia"             : etnia.nombre,
            "resguardo"         : resguardo.nombre,
            "departamento"      : persona.departamento
        }
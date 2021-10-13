from ..models import       usuario;
from rest_framework                               import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = usuario.Usuario
        fields = ['id', 'password', 'nombre', 'email', 'is_staff']

    def create(self, validated_data):
        userInstance = usuario.Usuario.objects.create_user(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user   = usuario.Usuario.objects.get(id = obj.id)
        return {
            "nombre" : user.nombre,
            "email" : user.email,
            "administrador": user.is_staff
        }
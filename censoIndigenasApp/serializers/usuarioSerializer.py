from ..models import       usuario;
from rest_framework                               import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = usuario.Usuario
        fields = ['id', 'username', 'password', 'name', 'email',]
    def create(self, validated_data):
        userInstance = usuario.Usuario.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user   = usuario.Usuario.objects.get(id=obj.id)
        return {
            "username" : user.username,
            "name" : user.name,
            "email" : user.email,
        }
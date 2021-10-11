from ..models import       usuario;
from rest_framework                               import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = usuario.Usuario
        fields = ['id', 'password', 'name', 'email',]
    def create(self, validated_data):
        userInstance = usuario.Usuario.objects.create_user(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user   = usuario.Usuario.objects.get(id=obj.id)
        return {
           
            "name" : user.name,
            "email" : user.email,
        }
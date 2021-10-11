from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.backends import TokenBackend

from ..models import Usuario
from ..serializers import UserSerializer



class UsuarioLista(APIView):
    def get(self, request):

        # Extraer info del token recibido
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        token         = request.META.get('HTTP_AUTHORIZATION')[7:]
        info_token    = token_backend.decode(token, verify=False) # Que hace el verify?

        # Extraer informacion de usuario loggeado
        usuario_token_id = info_token["user_id"]
        usuario = Usuario.objects.get_object(usuario_token_id)
        usuario_serializer = UserSerializer(usuario)

        # Verificar que el usuario tiene permisos de hacer el get, i.e. es administrador
        if not usuario_serializer.data["is_superuser"]:
            return Response({"detail": "Debe ser superusuario para acceder a la lista de usuarios"}, status = status.HTTP_401_UNAUTHORIZED)

        # Devolver lista de usuarios
        lista_usuarios = Usuario.objects.all()
        serializer = UserSerializer(lista_usuarios, many = True)
        return Response(serializer.data)

    def post(self, request, format = "JSON"):
        pass

class UsuarioDetalle(APIView):
    pass
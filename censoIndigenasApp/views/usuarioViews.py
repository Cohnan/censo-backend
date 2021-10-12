from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework_simplejwt.backends import TokenBackend

from ..models import Usuario
from ..serializers import UserSerializer



class UsuarioLista(APIView):
    '''
    Vista para la administracion de Usuarios, de parte de un usuario administrador
    '''
    # Para verificar antes de cada método que estos permiso (IsAuthenticated) se tiene
    # (y así no tener que hacer manualmente la verificación de que haya un Bearer token)
    # Y que la columna is_staff sea true (IsAdminUser)
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        '''
        Traer lista de usuarios
        '''

        # Extraer el token el "Bearer <token>"
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        
        print(f"\n\n UsuarioLista|get|request.META.get('HTTP_AUTHORIZATION'):\n{request.META.get('HTTP_AUTHORIZATION')} \n\n")

        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) # Setup parser
        
        info_token    = token_backend.decode(token, verify=False) # Que hace el verify?

        print(f"\n\n UsuarioLista|get|info_token (token_backend.decode(token):\n{info_token} \n\n")


        # Extraer informacion de usuario loggeado
        usuario_token_id = info_token["user_id"]
        usuario = Usuario.objects.get(id = usuario_token_id)
        usuario_serializer = UserSerializer(usuario)

        print(f"\n\n UsuarioLista|get|usuario_serializer.data:\n{usuario_serializer.data} \n\n")

        # Devolver lista de usuarios
        lista_usuarios = Usuario.objects.all()
        serializer = UserSerializer(lista_usuarios, many = True)

        return Response(serializer.data)

    def post(self, request, format = None):
        '''
        Crear nuevo usuario
        '''

        print("\n\nUser View | post | request.data\n")
        print(request.data)

        serializer = UserSerializer(data = request.data) # Realiza validacion, para solo hacer uso de atributos en la Metadata del UserSerializer

        if serializer.is_valid():
            serializer.save() # Guardar en base de datos
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response({"detail": "No se pudo crear el usuario", "errors": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

class UsuarioDetalle(APIView):
    pass

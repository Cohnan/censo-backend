from django.conf import settings
from django.http import Http404

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
    # Para verificar antes de cada método que se tiene el permiso IsAuthenticated
    # (y así no tener que hacer manualmente la verificación de que haya un Bearer token (código comentado en get),
    # y de que éste esté vigente )
    # Y que la columna is_staff sea true (IsAdminUser)
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        '''
        Traer lista de usuarios
        '''

        # # Extraer el token el "Bearer <token>"
        # try :
        #     token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # except:
        #     return Response({"detail": "Se necesita proveer un Bearer Token para autenticacion."}, status = status.HTTP_401_UNAUTHORIZED)

        # Devolver lista de usuarios
        lista_usuarios = Usuario.objects.all()
        serializer = UserSerializer(lista_usuarios, many = True) # Lista de Jsons con la informacion de cada uno

        return Response(serializer.data)

    def post(self, request, format = None):
        '''
        Crear nuevo usuario
        '''

        # request.data: Cuerpo completo de la peticion HTTP
        serializer = UserSerializer(data = request.data) # Conserva solo los atributos en la Metadata del UserSerializer -> validated_data, usado en creates del serializador

        if serializer.is_valid():
            serializer.save() # Guardar en base de datos
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response({"detail": "No se pudo crear el usuario", "errors": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

class UsuarioDetalle(APIView):
    '''
    Gestionar a un usuario
    '''

    # Antes de cada metodo: verificar que se esta proveyendo token en la HTTP Request
    permission_classes = (IsAuthenticated,)

    def get_object(self, id):
        '''
        Extraer modelo de usuario identificado por id dado
        '''
        try:
            return Usuario.objects.get(id=id) # Query SELECT * WHERE id=id
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        '''
        Tramitar peticion de Retorno de usuario identificado por id dado
        '''

        # 
        usuario = self.get_object(id)
        serializer = UserSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        '''
        Tramitar peticion de Actualizacion de usuario identificado por id dado
        '''
        pass 

    def delete(self, request, id, format=None):
        '''
        Tramitar peticion de Eliminacion de usuario identificado por id dado
        '''


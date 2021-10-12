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
    # Verifica antes de cada método que:
    # - IsAuthenticated: se aporto un token de acceso, y éste está vigente
    # - IsAdminUser: que es usuario administrador, es decir, que la columna is_staff sea True
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        '''
        Traer lista de usuarios
        '''
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
    # Verifica antes de cada método que:
    # - IsAuthenticated: se aporto un token de acceso, y éste está vigente
    # - IsAdminUser: que es usuario administrador, es decir, que la columna is_staff sea True
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_object(self, id):
        '''
        Extraer modelo de usuario identificado por id dado
        '''
        try:
            return Usuario.objects.get(id=id) # Query SELECT * WHERE id=id
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, id_usuario_url, format=None):
        '''
        Tramitar peticion de Retorno de usuario identificado por id dado
        '''
        # Traer informacion pedida
        usuario = self.get_object(id_usuario_url)
        serializer = UserSerializer(usuario)

        return Response(serializer.data)

    def put(self, request, id_usuario_url, format=None):
        '''
        Tramitar peticion de Actualizacion de usuario identificado por id dado
        '''
        usuario = self.get_object(id_usuario_url)
        serializer = UserSerializer(usuario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_usuario_url, format=None):
        '''
        Tramitar peticion de Eliminacion de usuario identificado por id dado
        '''
        usuario = self.get_object(id_usuario_url)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UsuarioPersonalizado(APIView):
    '''
    View para gestion de informacion propia
    '''
    # Verifica antes de cada método que:
    # - IsAuthenticated: se aporto un token de acceso, y éste está vigente
    permission_classes = (IsAuthenticated,)

    def get_object(self, id):
        '''
        Extraer modelo de usuario identificado por id dado
        '''
        try:
            return Usuario.objects.get(id=id) # Query SELECT * WHERE id=id
        except Usuario.DoesNotExist:
            raise Http404

    def extraer_info_loggeado(self, request):
        '''
        Clase ayudante para extraer info del usuario que hace la peticion
        '''

        # Extraer el "Bearer <token>"
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        
        # Extraer id del usuario duenio del token
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) # Setup parser
        info_token    = token_backend.decode(token, verify=False) # Que hace el verify?
        # info_token: metadata del token, que del usuario incluye (por defecto) solo el identificador unico del usuario creador en la llave user_id (ese nombre se configura en settings)

        # Extraer informacion de usuario duenio del token
        id_usuario_token = info_token["user_id"]
        usuario = self.get_object(id = id_usuario_token)
        usuario_serializer = UserSerializer(usuario)

        return id_usuario_token, usuario_serializer.data # Serializado del usuario duenio del token (producto de to_representation)

    def get(self, request):
        '''
        Tramitar peticion de Actualizacion de usuario autenticado
        '''
        id_us_log, _ = self.extraer_info_loggeado(request)

        # Traer informacion pedida
        usuario = self.get_object(id_us_log)
        serializer = UserSerializer(usuario)

        return Response(serializer.data)
        

    def put(self, request):
        '''
        Tramitar peticion de Actualizacion de usuario autenticado
        '''
        id_us_log, _ = self.extraer_info_loggeado(request)

        usuario = self.get_object(id_us_log)
        serializer = UserSerializer(usuario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        '''
        Tramitar peticion de Eliminacion de usuario identificado por id dado
        '''
        id_us_log, _ = self.extraer_info_loggeado(request)

        usuario = self.get_object(id_us_log)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
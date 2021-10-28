from django.http import Http404

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Etnia
from ..serializers import EtniaSerializer

class EtniaListaView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint etnias/
    '''
    # Solo permitir el procesamiento de estas peticiones a quienes han iniciado sesion
    permission_classes = (AllowAny, )

    def get(self, request):
        '''
        Permite traer la lista completa de etnias registradas 
        '''
        lista_etnias = Etnia.objects.all()
        serializer = EtniaSerializer(lista_etnias, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class EtniaCrearView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint etnias/agregar/
    '''
    # Permitir para cualquier etnia
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        '''
        Permite crear a una etnia identificada con el id dado, a partir de datos del formulario, codificados en un json
        '''
        serializer = EtniaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "detail": "Etnia registrada exitosamente.", 
            "registro": serializer.data
            }, status = status.HTTP_201_CREATED)
            
        return Response({
            "errors": serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)


class EtniaDetailView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint etnias/<id>
    '''
    # Solo permitir el procesamiento de estas peticiones a quienes han iniciado sesion
    permission_classes = (IsAuthenticated,  )

    def get_object(self, id):
        try:
            return Etnia.objects.get(id_etnia=id) # Query SELECT * WHERE id=id
        except Etnia.DoesNotExist:
            raise Http404

    def get(self, request, id_etnia_url, format=None):
        '''
        Permite traer detalles de etnia identificada con el id dado
        '''
        etnia = self.get_object(id_etnia_url)
        serializer = EtniaSerializer(etnia)
        return Response(serializer.data)

    def put(self, request, id_etnia_url, format=None):
        '''
        Permite actualizar detalles de etnia identificada con el id dado
        '''
        etnia = self.get_object(id_etnia_url)
        serializer = EtniaSerializer(etnia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "detail": "Etnia actualizada exitosamente.",
                "registro": serializer.data
                })

        return Response({
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_etnia_url, format=None):
        '''
        Permite borrar etnia identificada con el id dado
        '''
        etnia = self.get_object(id_etnia_url)
        etnia.delete()
        return Response({
            "detail": "Etnia eliminada exitosamente."
        }, status=status.HTTP_204_NO_CONTENT)

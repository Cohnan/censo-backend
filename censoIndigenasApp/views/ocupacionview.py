from django.http import Http404

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Ocupacion
from ..serializers import OcupacionSerializer

class OcupacionListaView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint ocupaciones/
    '''
    # Solo permitir el procesamiento de estas peticiones a quienes han iniciado sesion
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        '''
        Permite traer la lista completa de ocupaciones registradas 
        '''
        lista_ocupaciones = Ocupacion.objects.all()
        serializer = OcupacionSerializer(lista_ocupaciones, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class OcupacionCrearView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint ocupaciones/agregar/
    '''
    # Permitir para cualquier ocupacion
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        '''
        Permite crear a una ocupacion identificada con el id dado, a partir de datos del formulario, codificados en un json
        '''
        serializer = OcupacionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "detail": "Ocupacion registrada exitosamente.", 
            "registro": serializer.data
            }, status = status.HTTP_201_CREATED)
            
        return Response({
            "errors": serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)


class OcupacionDetailView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint ocupaciones/<id>
    '''
    # Solo permitir el procesamiento de estas peticiones a quienes han iniciado sesion
    permission_classes = (IsAuthenticated,  )

    def get_object(self, id):
        try:
            return Ocupacion.objects.get(id=id) # Query SELECT * WHERE id=id
        except Ocupacion.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        '''
        Permite traer detalles de ocupacion identificada con el id dado
        '''
        ocupacion = self.get_object(id)
        serializer = OcupacionSerializer(ocupacion)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        '''
        Permite actualizar detalles de ocupacion identificada con el id dado
        '''
        ocupacion = self.get_object(id)
        serializer = OcupacionSerializer(ocupacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "detail": "Ocupacion actualizada exitosamente.",
                "registro": serializer.data
                })

        return Response({
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        '''
        Permite borrar ocupacion identificada con el id dado
        '''
        ocupacion = self.get_object(id)
        ocupacion.delete()
        return Response({
            "detail": "Ocupacion eliminada exitosamente."
        }, status=status.HTTP_204_NO_CONTENT)

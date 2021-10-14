from django.http import Http404

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Resguardo
from ..serializers import ResguardoSerializer

class ResguardoListaView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint resguardos/
    '''
    # Solo permitir el procesamiento de estas peticiones a quienes han iniciado sesion
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        '''
        Permite traer la lista completa de resguardos registradas 
        '''
        lista_resguardos = Resguardo.objects.all()
        serializer = ResguardoSerializer(lista_resguardos, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class ResguardoCrearView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint resguardos/agregar/
    '''
    # Permitir para cualquier resguardo
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        '''
        Permite crear a una resguardo identificada con el id dado, a partir de datos del formulario, codificados en un json
        '''
        serializer = ResguardoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "detail": "Resguardo registrada exitosamente.", 
            "registro": serializer.data
            }, status = status.HTTP_201_CREATED)
            
        return Response({
            "errors": serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)


class ResguardoDetailView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint resguardos/<id>
    '''
    # Solo permitir el procesamiento de estas peticiones a quienes han iniciado sesion
    permission_classes = (IsAuthenticated,  )

    def get_object(self, id):
        try:
            return Resguardo.objects.get(id=id) # Query SELECT * WHERE id=id
        except Resguardo.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        '''
        Permite traer detalles de resguardo identificada con el id dado
        '''
        resguardo = self.get_object(id)
        serializer = ResguardoSerializer(resguardo)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        '''
        Permite actualizar detalles de resguardo identificada con el id dado
        '''
        resguardo = self.get_object(id)
        serializer = ResguardoSerializer(resguardo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "detail": "Resguardo actualizada exitosamente.",
                "registro": serializer.data
                })

        return Response({
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        '''
        Permite borrar resguardo identificada con el id dado
        '''
        resguardo = self.get_object(id)
        resguardo.delete()
        return Response({
            "detail": "Resguardo eliminada exitosamente."
        }, status=status.HTTP_204_NO_CONTENT)

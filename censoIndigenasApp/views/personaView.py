from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
#from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView # Averiguar
from rest_framework.response import Response
from rest_framework import status

from ..models import Persona
from ..serializers import PersonaSerializer

class PersonaList(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint censoIndigena/personas/
    '''
    # Solo permitir el procesamiento de estas peticiones a quienes han iniciado sesion
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        '''
        Permite traer la lista completa de personas registradas 
        '''
        lista_personas = Persona.objects.all()
        serializer = PersonaSerializer(lista_personas, many = True)
        return Response(serializer.data)

class PersonaCrearView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint censoIndigena/personas/censar/
    '''
    # Permitir para cualquier persona
    permissions_classes = (AllowAny, )

    def post(self, request, format=None):
        '''
        Permite crear a una persona identificada con el id dado, a partir de datos del formulario, codificados en un json
        '''
        serializer = PersonaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PersonaDetail(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint censoIndigena/personas/<id>
    '''
    # Solo permitir el procesamiento de estas peticiones a quienes han iniciado sesion
    permission_classes = (IsAuthenticated,  )

    def get_object(self, id):
        try:
            return Persona.objects.get(id=id) # Query SELECT * WHERE id=id
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        '''
        Permite traer detalles de persona identificada con el id dado
        '''
        persona = self.get_object(id)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        '''
        Permite actualizar detalles de persona identificada con el id dado
        '''
        persona = self.get_object(id)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        '''
        Permite borrar persona identificada con el id dado
        '''
        persona = self.get_object(id)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
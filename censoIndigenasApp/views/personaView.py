from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
#from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Persona
from ..serializers import PersonaSerializer

class PersonaListaView(APIView):
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
        return Response(serializer.data, status = status.HTTP_200_OK)

class PersonaCrearView(APIView):
    '''
    Procesa las peticiones que se hagan en el endpoint censoIndigena/personas/censar/
    '''
    # Permitir para cualquier persona
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        '''
        Permite crear a una persona identificada con el id dado, a partir de datos del formulario, codificados en un json
        '''
        serializer = PersonaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "detail": "Persona registrada exitosamente.", 
            "registro": serializer.data
            }, status = status.HTTP_201_CREATED)
            
        return Response({
            "errors": serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)


class PersonaDetailView(APIView):
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
            return Response({
                "detail": "Persona actualizada exitosamente.",
                "registro": serializer.data
                })

        return Response({
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        '''
        Permite borrar persona identificada con el id dado
        '''
        persona = self.get_object(id)
        persona.delete()
        return Response({
            "detail": "Persona eliminada exitosamente."
        }, status=status.HTTP_204_NO_CONTENT)

class PersonaBuscarDocView(APIView):
    '''
    Procesa peticiones de búsqueda de personas por su documento único de identificación
    '''

    # Solo permitir el procesamiento de estas peticiones a quienes han iniciado sesión
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        # Extraer documento de la peticion
        try:
            tipo_doc_req = request.data["tipo_doc"]
            numero_doc_req = request.data["doc_id"]
        except:
            return Response({"detail": "Formato de búsqueda inválido"}, status = status.HTTP_400_BAD_REQUEST)

        # Traer a la persona
        try:
            persona = Persona.objects.get(tipo_doc = tipo_doc_req, doc_id = numero_doc_req)
        except Persona.DoesNotExist:
            return Response({"detail": "Persona no encontrada"}, status = status.HTTP_404_NOT_FOUND)

        # Serializar a la persona corresopndiente para enviarlo como respuesta
        serializer = PersonaSerializer(persona)
        return Response(serializer.data, status = status.HTTP_200_OK)


        
        

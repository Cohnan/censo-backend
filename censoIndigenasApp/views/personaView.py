from django.shortcuts import render

#from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView # Averiguar
from rest_framework.response import Response
from rest_framework import status

from ..models import Persona
from ..serializers import PersonaSerializer

class PersonaList(APIView):
    def get(self, request):
        lista_personas = Persona.objects.all()
        serializer = PersonaSerializer(lista_personas, many = True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PersonaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class PersonaDetail(APIView):
    def get_object(self, id):
        try:
            return Persona.objects.get(id=id) # Query SELECT * WHERE id=id
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        persona = self.get_object(id)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)
    
from django.shortcuts import render

from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from rest_framework.views import APIView # Averiguar
from rest_framework.response import Response

from ..models import Persona
from ..serializers import PersonaSerializer

class PersonaList(APIView):
    def get(self, request):
        lista_personas = Persona.objects.all()
        serializer = PersonaSerializer(lista_personas, many = True)
        return Response(serializer.data)
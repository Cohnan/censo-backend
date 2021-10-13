from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated
#from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView # Averiguar
from rest_framework.response import Response
from rest_framework import status

from ..models import etnia
from ..serializers import etniaSerializer

class EtniaList(APIView):
    permission_classes = (IsAuthenticated )
    def get(self, request):
        lista_personas = etnia.objects.all()
        serializer = etniaSerializer(lista_personas, many = True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = etniaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class etniaDetail(APIView):
    permission_classes = (IsAuthenticated  )
    def get_object(self, id):
        try:
            return etnia.objects.get(id=id) # Query SELECT * WHERE id=id
        except etnia.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        persona = self.get_object(id)
        serializer = etniaSerializer(persona)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        persona = self.get_object(id)
        serializer = etniaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        persona = self.get_object(id)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
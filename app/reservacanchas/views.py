from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Ocupaciones, Personas
from reservacanchas import serializers


class OcupacionViewSet(viewsets.ModelViewSet):
    """View de Ocupacion APIs"""
    serializer_class = serializers.OcupacionSerializer
    queryset = Ocupaciones.objects.all()

    def list(self, request):
        queryset = Ocupaciones.objects.all()
        serializer = serializers.OcupacionSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})


class PersonasViewSet(viewsets.ModelViewSet):
    """View de Personas APIs"""
    serializer_class = serializers.PersonaSerializer
    queryset = Personas.objects.all()

    def list(self, request):
        queryset = Personas.objects.all()
        serializer = serializers.PersonaSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

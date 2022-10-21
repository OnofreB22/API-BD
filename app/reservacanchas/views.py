from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from core.models import (
    Ocupaciones,
    Personas,
    Canchas,
    Implementos,
    Reserva
    )

from reservacanchas import serializers


class OcupacionViewSet(viewsets.ModelViewSet):
    """View de Ocupacion APIs"""
    serializer_class = serializers.OcupacionSerializer
    queryset = Ocupaciones.objects.all()


class PersonasViewSet(viewsets.ModelViewSet):
    """View de Personas APIs"""
    serializer_class = serializers.PersonaSerializer
    queryset = Personas.objects.all()

    def list(self, request):
        queryset = Personas.objects.all()
        serializer = serializers.PersonaSerializer(queryset, many=True)
        return Response(serializer.data)


class CanchasViewSet(viewsets.ModelViewSet):
    """View de Canchas APIs"""
    serializer_class = serializers.CanchaSerializer
    queryset = Canchas.objects.all()

    def list(self, request):
        queryset = Canchas.objects.all()
        serializer = serializers.CanchaSerializer(queryset, many=True)
        return Response(serializer.data)


class ImplementosViewSet(viewsets.ModelViewSet):
    """View de Implementos APIs"""
    serializer_class = serializers.ImplementoSerializer
    queryset = Implementos.objects.all()

    def list(self, request):
        queryset = Implementos.objects.all()
        serializer = serializers.ImplementoSerializer(queryset, many=True)
        return Response(serializer.data)


class ReservasViewSet(viewsets.ModelViewSet):
    """View de Reserva APIs"""
    serializer_class = serializers.ReservaSerializer
    queryset = Reserva.objects.all()

    def list(self, request):
        queryset = Reserva.objects.all()
        serializer = serializers.ReservaSerializer(queryset, many=True)
        return Response(serializer.data)

from rest_framework import viewsets

from core.models import Ocupaciones
from ocupacion import serializers


class OcupacionViewSet(viewsets.ModelViewSet):
    """View de Ocupacion APIs"""
    serializer_class = serializers.OcupacionSerializer
    queryset = Ocupaciones.objects.all()

    def get_queryset(self):
        "Retrieve ocupaciones"
        return self.queryset.filter(idocupaciones=self.request.idocupaciones)

    def perform_create(self, serializer):
        "Create ocupaciones"
        serializer.save()

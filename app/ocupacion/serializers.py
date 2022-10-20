"""
Serializer de ocupacion API View
"""
from rest_framework import serializers

from core.models import Ocupaciones


class OcupacionSerializer(serializers.ModelSerializer):
    """Serializer del objeto ocupacion"""

    class Meta:
        model = Ocupaciones
        fields = [
            'idocupaciones',
            'departamanto',
            'carrera',
            'persona_exterior']

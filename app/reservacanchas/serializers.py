"""
Serializer de ocupacion API View
"""
from rest_framework import serializers

from core.models import Ocupaciones, Personas


class OcupacionSerializer(serializers.ModelSerializer):
    """Serializer del objeto ocupacion"""

    class Meta:
        model = Ocupaciones
        fields = [
            'id',
            'departamento',
            'carrera',
            'persona_exterior']


class PersonaSerializer(serializers.ModelSerializer):
    """Serializer del objeto persona"""

    class Meta:
        model = Personas
        fields = [
            'cedula',
            'nombre',
            'apellido',
            'numero_de_celular',
            'correo',
            'tipo_de_ocupacion',
            'genero',
            'ocupacion',
        ]

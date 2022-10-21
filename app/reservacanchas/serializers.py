"""
Serializer de ocupacion API View
"""
from rest_framework import serializers

from core.models import (
    Ocupaciones,
    Personas,
    Canchas,
    Implementos,
    Reserva
    )


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


class CanchaSerializer(serializers.ModelSerializer):
    """Serializer del objeto cancha"""

    class Meta:
        model = Canchas
        fields = [
            'id',
            'tipo_cancha',
            'material',
            'ubicacion',
            'tamano',
        ]

class ImplementoSerializer(serializers.ModelSerializer):
    """Serializer del objeto implemento"""

    class Meta:
        model = Implementos
        fields = [
            'id',
            'codigo_cancha',
            'balon',
            'red',
            'arco',
        ]

class ReservaSerializer(serializers.ModelSerializer):
    """Serializer del objeto reserva"""

    class Meta:
        model = Reserva
        fields = [
            'id',
            'personas_cedula',
            'disponibilidad',
            'fecha_reserva',
            'canchas_codigo',
        ]

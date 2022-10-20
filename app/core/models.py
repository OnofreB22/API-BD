"""
Modelos de la base de datos de reserva de cancahs
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Ocupaciones(models.Model):

    class PersonaExterior(models.TextChoices):
        SI = 'SI', _('SI')
        NO = 'NO', _('NO')

    departamento = models.CharField(max_length=45)
    carrera = models.CharField(max_length=45)
    persona_exterior = models.CharField(
        max_length=2,
        choices=PersonaExterior.choices,
        default=PersonaExterior.NO
        )

    def __str__(self):
        return self.departamento


class Personas(models.Model):

    cedula = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    numero_de_celular = models.BigIntegerField()
    correo = models.CharField(max_length=100)
    tipo_de_ocupacion = models.CharField(max_length=15)
    genero = models.CharField(max_length=30)
    ocupacion = models.ForeignKey(Ocupaciones, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Canchas(models.Model):

    class TipoCancha(models.TextChoices):
        tenis = 'Tenis de campo', _('Tenis de campo')
        baloncesto = 'Baloncesto', _('Baloncesto')
        voleibol = 'Voleibol', _('Voleibol')
        futbol = 'Futbol Sala', _('Futbol Sala')

    tipo_cancha = models.CharField(max_length=20, choices=TipoCancha.choices)
    material = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=45)
    tamano = models.IntegerField()

    def __str__(self):
        return self.tipo_cancha


class Implementos(models.Model):

    codigo_cancha = models.ForeignKey(Canchas, on_delete=models.CASCADE)
    balon = models.SmallIntegerField()
    red = models.CharField(max_length=10)
    arco = models.CharField(max_length=10)


class Reserva(models.Model):

    class Disponibilidad(models.TextChoices):
        SI = 'SI', _('Si')
        NO = 'NO', _('NO')

    personas_cedula = models.ForeignKey(Personas, on_delete=models.CASCADE)
    disponibilidad = models.CharField(
        max_length=2,
        choices=Disponibilidad.choices,
        default=Disponibilidad.SI
        )
    fecha_reserva = models.DateTimeField()
    canchas_codigo = models.ForeignKey(Canchas, on_delete=models.CASCADE)

"""
Test para los modelos
"""
from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_create_ocupacion(self):
        """Test creacion de ocupacion exitosa"""
        ocupacion = models.Ocupaciones.objects.create(
            departamento='Ingenieria',
            carrera='Ing. Sistemas',
            persona_exterior='SI',
        )

        self.assertEqual(str(ocupacion), ocupacion.departamento)

    def test_create_persona(self):
        """Test creacion de persona exitosa"""
        ocupacion = models.Ocupaciones.objects.create(
            departamento='Ciencias',
            carrera='Ing. Sistemas',
            persona_exterior='SI',
        )
        persona = models.Personas.objects.create(
            cedula=1006739192,
            nombre='Onofre',
            apellido='Benjumea',
            numero_de_celular=3137601600,
            correo='oabenjumev@gmail.com',
            tipo_de_ocupacion='Estudiante',
            genero='Masculino',
            ocupacion=ocupacion,
        )

        self.assertEqual(str(persona), persona.nombre)
        self.assertEqual(persona.ocupacion, ocupacion)

    def test_create_cancha(self):
        """Test creacion de cancha exitosa"""
        cancha = models.Canchas.objects.create(
            tipo_cancha='Tenis de campo',
            material='grama',
            ubicacion='Eafit',
            tamano=50,
        )

        self.assertEqual(str(cancha), cancha.tipo_cancha)

    def test_create_implemento(self):
        """Test creacion de implementos exitosa"""
        cancha = models.Canchas.objects.create(
            tipo_cancha='Tenis de campo',
            material='grama',
            ubicacion='Eafit',
            tamano=50,
        )
        implementos = models.Implementos.objects.create(
            codigo_cancha=cancha,
            balon=1,
            red='no',
            arco='si',
        )

        self.assertEqual(cancha, implementos.codigo_cancha)

    def test_create_reserva(self):
        """Test creacion de reserva exitosa"""
        ocupacion = models.Ocupaciones.objects.create(
            departamento='Ciencias',
            carrera='Ing. Sistemas',
            persona_exterior='SI',
        )
        persona = models.Personas.objects.create(
            cedula=1006739192,
            nombre='Onofre',
            apellido='Benjumea',
            numero_de_celular=3137601600,
            correo='oabenjumev@gmail.com',
            tipo_de_ocupacion='Estudiante',
            genero='Masculino',
            ocupacion=ocupacion,
        )
        cancha = models.Canchas.objects.create(
            tipo_cancha='Tenis de campo',
            material='grama',
            ubicacion='Eafit',
            tamano=50,
        )
        reserva = models.Reserva.objects.create(
            personas_cedula=persona,
            disponibilidad='SI',
            fecha_reserva='2006-10-25 14:30:59',
            canchas_codigo=cancha,
        )

        self.assertEqual(reserva.personas_cedula, persona)
        self.assertEqual(reserva.canchas_codigo, cancha)
        self.assertEqual(reserva.fecha_reserva, '2006-10-25 14:30:59')

"""
Tests for recipe APIs.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from reservacanchas.serializers import OcupacionSerializer

from core.models import Ocupaciones


def create_ocupacion():
    payload = {
        'departamento': 'Ingenieria',
        'carrera': 'Ing. Sistemas',
        'persona_exterior': 'SI',
        }
    res = APIClient().post(
        reverse('reservacanchas:ocupacion-list'),
        payload
        )
    return res


class ReservaCanchasApiTests(TestCase):
    """Testea todos los endpoints de la api"""
    def setUp(self):
        self.client = APIClient()

    def test_create_ocupacion(self):
        """Testea que la creacion de una ocupacion sea exitosa"""
        payload = {
            'departamento': 'Ingenieria',
            'carrera': 'Ing. Sistemas',
            'persona_exterior': 'SI',
            }
        res = self.client.post(
            reverse('reservacanchas:ocupacion-list'),
            payload
            )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['departamento'], payload['departamento'])

    def test_delete_ocupacion(self):
        """Testea la elminacion exitosa de una ocupacion"""
        ocupacion = create_ocupacion()
        id = ocupacion.data['id']
        res = self.client.delete(
            reverse('reservacanchas:ocupacion-detail', args=[id])
            )

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Ocupaciones.objects.filter(id=id).exists())

    def test_get_ocupacion(self):
        """Testea la obtencion exitosa de una ocupacion"""
        ocupacion = create_ocupacion()
        id = ocupacion.data['id']
        res = self.client.get(
            reverse('reservacanchas:ocupacion-detail', args=[id])
            )
        object = OcupacionSerializer(Ocupaciones.objects.get(id=id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, object.data)

    def test_update_ocupacion(self):
        """Testea la actualizacon exitosa de una ocupacion"""
        ocupacion = create_ocupacion()
        id = ocupacion.data['id']
        payload = {'departamento': 'Ciencias'}
        res = self.client.patch(
            reverse('reservacanchas:ocupacion-detail', args=[id]),
            payload
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['departamento'], payload['departamento'])

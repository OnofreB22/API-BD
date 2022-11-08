from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

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

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Ocupaciones, id=item)

    def get_queryset(self):
        return Ocupaciones.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
            )

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        user_object = self.get_object()
        Ocupaciones.objects.filter(id=user_object.id).delete()
        user_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonasViewSet(viewsets.ModelViewSet):
    """View de Personas APIs"""
    serializer_class = serializers.PersonaSerializer
    queryset = Personas.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Personas, id=item)

    def get_queryset(self):
        return Personas.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
            )

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        user_object = self.get_object()
        Personas.objects.filter(id=user_object.id).delete()
        user_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CanchasViewSet(viewsets.ModelViewSet):
    """View de Canchas APIs"""
    serializer_class = serializers.CanchaSerializer
    queryset = Canchas.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Canchas, id=item)

    def get_queryset(self):
        return Canchas.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
            )

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        user_object = self.get_object()
        Canchas.objects.filter(id=user_object.id).delete()
        user_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImplementosViewSet(viewsets.ModelViewSet):
    """View de Implementos APIs"""
    serializer_class = serializers.ImplementoSerializer
    queryset = Implementos.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Implementos, id=item)

    def get_queryset(self):
        return Implementos.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
            )

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        user_object = self.get_object()
        Implementos.objects.filter(id=user_object.id).delete()
        user_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReservasViewSet(viewsets.ModelViewSet):
    """View de Reserva APIs"""
    serializer_class = serializers.ReservaSerializer
    queryset = Reserva.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Reserva, id=item)

    def get_queryset(self):
        return Reserva.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
            )

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        user_object = self.get_object()
        Reserva.objects.filter(id=user_object.id).delete()
        user_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

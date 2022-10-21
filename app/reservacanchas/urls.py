"""
URL mapping de ocupacion
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from reservacanchas import views


router = DefaultRouter()
router.register('ocupacion', views.OcupacionViewSet, basename='ocupacion')
router.register('personas', views.PersonasViewSet, basename='personas')
router.register('canchas', views.CanchasViewSet, basename='canchas')
router.register(
    'implementos',
    views.ImplementosViewSet,
    basename='implementos'
    )
router.register('reservas', views.ReservasViewSet, basename='reservas')

app_name = 'reservacanchas'

urlpatterns = [
    path('', include(router.urls)),
]

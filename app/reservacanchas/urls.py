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
router.register('ocupacion', views.OcupacionViewSet)
router.register('personas', views.PersonasViewSet)
router.register('canchas', views.CanchasViewSet)
router.register('implementos', views.ImplementosViewSet)
router.register('reservas', views.ReservasViewSet)


app_name = 'Reserva_Canchas'

urlpatterns = [
    path('', include(router.urls)),
]

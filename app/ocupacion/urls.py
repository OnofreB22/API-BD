"""
URL mapping de ocupacion
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from ocupacion import views


router = DefaultRouter()
router.register('ocupacion', views.OcupacionViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]

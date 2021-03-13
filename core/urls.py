from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import CardapioViewSet, AvaliacaoViewSet

router = SimpleRouter()
router.register('cardapios', CardapioViewSet)
router.register('avaliacao', AvaliacaoViewSet)
from django.urls import path
from .views import cotacoins, buscar_cotacao, cotacao, infos_grafico, grafico

urlpatterns = [
    path('', cotacoins, name='cotacoins'),
    path('buscar', buscar_cotacao, name='buscar_cotacao'),
    path('cotacao', cotacao, name='cotacao'),
    path('infos-grafico', infos_grafico, name='infos_grafico'),
    path('grafico', grafico, name='grafico'),
]
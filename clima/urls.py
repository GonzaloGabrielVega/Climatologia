from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_climatologica, name='vista_climatologica'), # SE CAMBIO LA RUTA PARA ACCEDER MAS RAPIDO SIN MODIFICAR LA URL
]

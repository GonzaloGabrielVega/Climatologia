from django.urls import path
from . import views

urlpatterns = [
    path('mostrar_tiempo_real',views.mostrar_tiempo_real,name='mostrar_tiempo_real'),
    path('obtener_datos',views.obtener_datos,name='obtener-datos'),
    path('', views.vista_climatologica, name='vista_climatologica'), # SE CAMBIO LA RUTA PARA ACCEDER MAS RAPIDO SIN MODIFICAR LA URL
]

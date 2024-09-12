from django.shortcuts import render
from .models import Climatologia
from django.http import JsonResponse
def vista_climatologica(request):
    datos = Climatologia.objects.all().order_by('fecha')
    
    # Extrae los datos en listas y convierte las fechas a cadenas en formato ISO
    fechas = [dato.fecha.strftime('%Y-%m-%dT%H:%M:%SZ') for dato in datos]
    temperaturas = list(datos.values_list('temperatura', flat=True))
    humedades = list(datos.values_list('humedad', flat=True))
    presiones = list(datos.values_list('presion', flat=True))
    velocidades_viento = list(datos.values_list('velocidad_viento', flat=True))

    contexto = {
        'fechas': fechas,
        'temperaturas': temperaturas,
        'humedades': humedades,
        'presiones': presiones,
        'velocidades_viento': velocidades_viento,
    }
    
    return render(request, 'climatologia.html', contexto)

def obtener_datos(request):
    datos = Climatologia.objects.all().order_by('fecha')

    # Extrae los datos en listas y convierte las fechas a cadenas en formato ISO
    fechas = [dato.fecha.strftime('%Y-%m-%dT%H:%M:%SZ') for dato in datos]
    temperaturas = list(datos.values_list('temperatura', flat=True))
    humedades = list(datos.values_list('humedad', flat=True))
    presiones = list(datos.values_list('presion', flat=True))
    velocidades_viento = list(datos.values_list('velocidad_viento', flat=True))

    contexto = {
        'fechas': fechas,
        'temperaturas': temperaturas,
        'humedades': humedades,
        'presiones': presiones,
        'velocidades_viento': velocidades_viento,
    }

    return JsonResponse(contexto)

def mostrar_tiempo_real(request):
    return render(request,'mostra_real.html') 
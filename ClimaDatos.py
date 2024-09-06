import random
from datetime import datetime, timedelta
import json

# Script para autogenerar datos climatologicos y guardarlos como .json 
def generar_datos_climatologia(cantidad):
    datos = []
    fecha_inicial = datetime(2024, 9, 1, 8, 0, 0)  # Fecha inicial
    for i in range(cantidad):
        fecha = fecha_inicial + timedelta(hours=24 * i)  # Datos cada 4 horas
        temperatura = round(random.uniform(25, 28), 1)  # Temperatura entre 18 y 28°C
        humedad = round(random.uniform(50, 65), 1)  # Humedad entre 50% y 75%
        presion = round(random.uniform(1008, 1016), 1)  # Presión entre 1008 y 1016 hPa
        velocidad_viento = round(random.uniform(8, 20), 1)  # Viento entre 8 y 20 km/h
        
        dato = { 
            "model": "clima.climatologia",
            "pk": i + 1,
            "fields": {
                "fecha": fecha.strftime('%Y-%m-%dT%H:%M:%SZ'),
                "temperatura": temperatura,
                "humedad": humedad,
                "presion": presion,
                "velocidad_viento": velocidad_viento
            }
        }
        datos.append(dato)
    
    return datos

# Generar 100 registros de datos
datos_climatologicos = generar_datos_climatologia(600)

# Guardar en un archivo JSON
with open('datos_climatologicos.json', 'w', encoding='utf-8') as archivo:
    json.dump(datos_climatologicos, archivo, ensure_ascii=False, indent=4)

print("Archivo JSON guardado exitosamente.")
from django.db import models

# Create your models here.
class Climatologia(models.Model):
    fecha = models.DateTimeField()
    temperatura = models.FloatField()
    humedad = models.FloatField()
    presion = models.FloatField()
    velocidad_viento = models.FloatField()

    def __str__(self):
        return f"Climatología del {self.fecha}"
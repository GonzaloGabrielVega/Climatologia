from django.db import models
from django.utils import timezone
# Create your models here.
class Climatologia(models.Model):
    fecha = models.DateTimeField(timezone.now)
    temperatura = models.FloatField()
    humedad = models.FloatField()
    presion = models.FloatField()
    velocidad_viento = models.FloatField()

    def __str__(self):
        return f"Climatología del {self.fecha}"
from django.db import models

class Avion(models.Model):
    Id_Avion = models.CharField(max_length=6, unique=True, primary_key=True)
    Modelo = models.CharField(max_length=100)
    Aerolinea = models.CharField(max_length=100)
    Capacidad_Asientos = models.IntegerField()  # No necesitas limitar aquí (los límites son manejados en el formulario)
    Capacidad_Carga = models.IntegerField()  # Incrementa los valores en el formulario
    Año_Fabricacion = models.CharField(max_length=4)
    Estado_Avion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
         return self.Modelo

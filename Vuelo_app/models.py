from django.db import models

class Vuelo(models.Model):
    Id_Vuelo = models.AutoField(primary_key=True)
    Id_Empleado = models.CharField(max_length=100)
    Numero_Vuelo = models.CharField(max_length=100)
    Origen = models.CharField(max_length=100)  # Asegúrate de que este campo exista
    Destino = models.CharField(max_length=100)
    Hora_llegada = models.TimeField()
    Hora_Salida = models.TimeField()
    Estado_Vuelo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Id_Vuelo)

from django.db import models

class Reserva(models.Model):
    Id_Reserva = models.AutoField(primary_key=True)  # Usar AutoField para autoincrementar
    Id_pasajero = models.CharField(max_length=100)
    Id_vuelo = models.CharField(max_length=100)
    Fecha_Reserva = models.DateField()  # Cambiar a DateField para manejar fechas
    Estado_reserva = models.CharField(max_length=100)
    Clase_Servicio = models.CharField(max_length=100)
    Numero_Reserva = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Id_Reserva)


from django.db import models

# Create your models here.

class Boleto(models.Model):
    Id_Boleto=models.CharField(primary_key=True,max_length=6)
    Id_Reserva=models.CharField(max_length=100)
    Numero_Boleto=models.CharField(max_length=100)
    Precio=models.CharField(max_length=100)
    Fecha_Emicion=models.CharField(max_length=100)
    Estado_Boleto=models.CharField(max_length=100)
    Clase_Servicio=models.CharField(max_length=100)

    def __str__(self) :
        return self.Numero_Boleto
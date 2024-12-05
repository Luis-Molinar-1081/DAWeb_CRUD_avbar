from django.db import models

# Create your models here.

class Pago(models.Model):
    Id_Pago=models.CharField(primary_key=True,max_length=6)
    Id_Pasagero=models.CharField(max_length=100)
    Id_Empleado=models.CharField(max_length=100)
    Id_Vuelo=models.CharField(max_length=100)
    Id_Boleto=models.CharField(max_length=100)
    Precio=models.CharField(max_length=100)
    Fecha_Pago=models.CharField(max_length=100)
    Metodo_Pago=models.CharField(max_length=100)
    Estado=models.CharField(max_length=100)

    def __str__(self) :
        return self.Id_Pago
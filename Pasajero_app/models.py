from django.db import models

class Pasajero(models.Model):
    Id_Pasagero = models.AutoField(primary_key=True)  # Usar AutoField para autoincrementar
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Numero_Documento = models.IntegerField()
    Nacionalidad = models.CharField(max_length=100)
    Fecha_de_Nacimiento = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre

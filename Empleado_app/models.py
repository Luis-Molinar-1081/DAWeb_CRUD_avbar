from django.db import models

# Create your models here.

class Empleado(models.Model):
    Id_Empleado=models.CharField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=100)
    Apellido=models.CharField(max_length=100)
    Genero=models.CharField(max_length=100)
    Fecha_de_Nacimiento=models.CharField(max_length=100)
    Nacionalidad=models.CharField(max_length=100)
    Telefono=models.CharField(max_length=100)
    Puesto=models.CharField(max_length=100)

    def __str__(self) :
        return self.Nombre
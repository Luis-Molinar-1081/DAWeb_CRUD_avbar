from django.shortcuts import render, redirect, get_object_or_404
from .models import Pasajero
# Create your views here.

# Vista para la página de inicio
def inicio_vista(request):
    ListadoPasajero = Pasajero.objects.all()
    return render(request, "GestionarPasajero.html", {"losPasajeros": ListadoPasajero})

# Vista para registrar Pasajeros
def registrarPasagero(request):
    if request.method == 'POST':
        Id_Pasagero = request.POST["txtId_Pasagero"]
        Nombre = request.POST["txtNombre"]
        Apellido = request.POST["txtApellido"]
        Numero_Documento = request.POST["numNumero_Documento"]
        Nacionalidad = request.POST["txtNacionalidad"]
        Fecha_de_Nacimiento = request.POST["txtFecha_de_Nacimiento"]
        Telefono = request.POST["txtTelefono"]
        
        # Verificar si el Id_Pasagero ya existe
        if Pasajero.objects.filter(Id_Pasagero=Id_Pasagero).exists():
            # Si ya existe, devolver el formulario con un mensaje de error
            return render(request, "GestionarPasajero.html", {"error": "El ID de Pasajero ya existe."})
        
        # Si no existe, guardar el nuevo pasajero
        Pasajero.objects.create(
            Id_Pasagero=Id_Pasagero,
            Nombre=Nombre,
            Apellido=Apellido,
            Numero_Documento=Numero_Documento,
            Nacionalidad=Nacionalidad,
            Fecha_de_Nacimiento=Fecha_de_Nacimiento,
            Telefono=Telefono
        )
        return redirect("Pasajero")  # Redirigir después de guardar

    return render(request, "GestionarPasajero.html")

def seleccionarPasagero(request,Id_Pasagero):
    pasajero = Pasajero.objects.get(Id_Pasagero=Id_Pasagero)  # Usar 'pasajero' en minúsculas
    return render(request, "editarPasajero.html", {"misPasajeros": pasajero})

def editarPasagero(request):
    if request.method == 'POST':
        # Obtiene los datos del formulario
        Id_Pasagero = request.POST['txtId_Pasagero']
        pasajero = get_object_or_404(Pasajero, Id_Pasagero=Id_Pasagero)
        
        # Actualiza los campos del pasajero con los nuevos valores del formulario
        pasajero.Nombre = request.POST['txtNombre']
        pasajero.Apellido = request.POST['txtApellido']
        pasajero.Numero_Documento = int(request.POST['numNumero_Documento'])
        pasajero.Nacionalidad = request.POST['txtNacionalidad']
        pasajero.Fecha_de_Nacimiento = request.POST['txtFecha_de_Nacimiento']
        pasajero.Telefono = request.POST['txtTelefono']
        
        # Guarda los cambios en la base de datos
        pasajero.save()
        
        # Redirige al listado de pasajeros
        return redirect('Pasajero')
    else:
        # Si no es un POST, redirige a la página de inicio
        return redirect('Pasajero')

def borrarPasagero(request, Id_Pasagero):
    try:
        pasajero = Pasajero.objects.get(Id_Pasagero=Id_Pasagero)
        pasajero.delete()  
        return redirect("Pasajero")  # Redirige a la vista principal
    except pasajero.DoesNotExist:
        return render(request, "error.html", {"mensaje": "El pasajero no existe"})

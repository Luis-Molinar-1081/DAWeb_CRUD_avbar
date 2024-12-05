from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado  # Asegúrate de que este es el modelo correcto

# Vista para la página de inicio
def inicio_vista(request):
    ListadoEmpleado = Empleado.objects.all()  # Obtiene todos los empleados
    return render(request, "GestionarEmpleado.html", {"losEmpleados": ListadoEmpleado})

# Vista para registrar Empleado
def registrarEmpleado(request):
    if request.method == 'POST':  # Verifica si la solicitud es POST
        Id_Empleado = request.POST["txtId_Empleado"]
        Nombre = request.POST["txtNombre"]
        Apellido = request.POST["txtApellido"]
        Genero = request.POST["txtGenero"]
        Fecha_de_Nacimiento = request.POST["txtFecha_de_Nacimiento"]
        Nacionalidad = request.POST["txtNacionalidad"]
        Telefono = request.POST["txtTelefono"]
        Puesto = request.POST["txtPuesto"]

        # Verificar si el ID de empleado ya existe
        if Empleado.objects.filter(Id_Empleado=Id_Empleado).exists():
            # Si ya existe, devolver el formulario con un mensaje de error
            return render(request, "GestionarEmpleado.html", {"error": "El ID de Empleado ya existe."})
        
        # Si no existe, guardar el nuevo empleado
        Empleado.objects.create(
            Id_Empleado=Id_Empleado,
            Nombre=Nombre,
            Apellido=Apellido,
            Genero=Genero,
            Fecha_de_Nacimiento=Fecha_de_Nacimiento,
            Nacionalidad=Nacionalidad,
            Telefono=Telefono,
            Puesto=Puesto
        )
        return redirect("Empleado")  # Redirigir después de guardar

    return render(request, "GestionarEmpleado.html")

def seleccionarEmpleado(request, Id_Empleado):
    empleado = get_object_or_404(Empleado, Id_Empleado=Id_Empleado)  # Obtén el empleado
    return render(request, "editarEmpleado.html", {"empleado": empleado})  # Renderiza la plantilla adaptada



# Vista para editar los datos del empleado
def editarEmpleado(request, Id_Empleado):
    empleado = get_object_or_404(Empleado, Id_Empleado=Id_Empleado)  # Obtén el empleado por su ID

    if request.method == 'POST':  # Solo procesa si es una solicitud POST
        # Actualiza los campos del empleado con los datos del formulario
        empleado.Nombre = request.POST['txtNombre']
        empleado.Apellido = request.POST['txtApellido']
        empleado.Genero = request.POST['txtGenero']
        empleado.Fecha_de_Nacimiento = request.POST['txtFecha_de_Nacimiento']
        empleado.Nacionalidad = request.POST['txtNacionalidad']
        empleado.Telefono = request.POST['txtTelefono']
        empleado.Puesto = request.POST['txtPuesto']

        # Guarda los cambios en la base de datos
        empleado.save()

        # Redirige al listado de empleados después de guardar
        return redirect('Empleado')  # O a una vista específica si es necesario

    # Si no es un POST, muestra el formulario con los datos actuales
    return render(request, "editarEmpleado.html", {"empleado": empleado})



# Vista para borrar un empleado
def borrarEmpleado(request, Id_Empleado):
    try:
        # Busca el empleado usando el modelo `Empleado`
        empleado = get_object_or_404(Empleado, Id_Empleado=Id_Empleado)
        empleado.delete()  # Elimina el empleado
        return redirect("Empleado")  # Redirige a la vista principal
    except Empleado.DoesNotExist:
        # Maneja el caso donde no existe el empleado
        return render(request, "error.html", {"mensaje": "El empleado no existe"})

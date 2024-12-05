from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva  # Asegúrate de que este es el modelo correcto

# Vista para la página de inicio
def inicio_vista(request):
    reservas = Reserva.objects.all()  # Obtener todas las reservas
    return render(request, 'GestionarReserva.html', {'reservas': reservas})



# Vista para registrar una reserva
def registrarReserva(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        id_pasajero = request.POST.get('txtId_pasajero')
        id_vuelo = request.POST.get('txtId_vuelo')
        fecha_reserva = request.POST.get('txtFecha_Reserva')
        estado_reserva = request.POST.get('txtEstado_reserva')
        clase_servicio = request.POST.get('txtClase_Servicio')
        numero_reserva = request.POST.get('txtNumero_Reserva')

        # Crear un objeto Reserva con los datos
        reserva = Reserva(
            Id_pasajero=id_pasajero,
            Id_vuelo=id_vuelo,
            Fecha_Reserva=fecha_reserva,
            Estado_reserva=estado_reserva,
            Clase_Servicio=clase_servicio,
            Numero_Reserva=numero_reserva
        )

        # Guardar la reserva en la base de datos
        reserva.save()

    # Obtener todas las reservas de la base de datos
    reservas = Reserva.objects.all()

    # Renderizar la plantilla y pasar las reservas a la vista
    return render(request, 'GestionarReserva.html', {'reservas': reservas})


# Vista para seleccionar la reserva para editar
def seleccionarReserva(request, id_reserva):
    reserva = get_object_or_404(Reserva, Id_Reserva=id_reserva)  # Obtén la reserva
    return render(request, "editarReserva.html", {"reserva": reserva})  # Renderiza la plantilla adaptada

# Vista para editar los datos de la reserva
def editarReserva(request, id):
    # Recupera la reserva con el id proporcionado
    reserva = get_object_or_404(Reserva, pk=id)

    # Verifica si el formulario fue enviado (en caso de edición)
    if request.method == 'POST':
        # Obtener los datos del formulario
        reserva.Id_pasajero = request.POST.get('txtId_pasajero')
        reserva.Id_vuelo = request.POST.get('txtId_vuelo')
        reserva.Fecha_Reserva = request.POST.get('txtFecha_Reserva')
        reserva.Estado_reserva = request.POST.get('txtEstado_reserva')
        reserva.Clase_Servicio = request.POST.get('txtClase_Servicio')
        reserva.Numero_Reserva = request.POST.get('txtNumero_Reserva')

        # Guarda los cambios de la reserva
        reserva.save()

        # Redirige al listado de reservas después de editar
        return redirect("Reserva")  # Redirige al inicio después de editar

    # Si el formulario no fue enviado, se muestra el formulario de edición
    return render(request, 'editarReserva.html', {'reserva': reserva})


# Vista para borrar una reserva
def borrarReserva(request, Id_Reserva):
    reserva = get_object_or_404(Reserva, Id_Reserva=Id_Reserva)  # Encuentra la reserva
    reserva.delete()  # Elimina la reserva de la base de datos
    return redirect('Reserva')  # Redirige a la vista principal para actualizar la tabla

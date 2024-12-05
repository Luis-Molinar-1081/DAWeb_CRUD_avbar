from django.shortcuts import render, redirect, get_object_or_404
from .models import Vuelo

# Vista para mostrar todos los vuelos
def inicio_vista(request):
    vuelos = Vuelo.objects.all()  # Obtener todos los vuelos almacenados
    return render(request, 'GestionarVuelo.html', {'vuelos': vuelos})

# Vista para gestionar los vuelos (esto será la misma vista de inicio_vista)
def GestionarVuelo(request):
    vuelos = Vuelo.objects.all()  # Obtener todos los vuelos almacenados
    return render(request, 'GestionarVuelo.html', {'vuelos': vuelos})

# Vista para registrar un nuevo vuelo
def registrarVuelo(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        Id_Empleado = request.POST.get('txtId_Empleado')
        Numero_Vuelo = request.POST.get('txtNumero_Vuelo')
        Origen = request.POST.get('txtOrigen')
        Destino = request.POST.get('txtDestino')
        Hora_llegada = request.POST.get('txtHora_llegada')
        Hora_Salida = request.POST.get('txtHora_Salida')
        Estado_Vuelo = request.POST.get('txtEstado_Vuelo')

        # Validar si todos los campos están presentes
        if not (Id_Empleado and Numero_Vuelo and Origen and Destino and Hora_llegada and Hora_Salida and Estado_Vuelo):
            return render(request, 'GestionarVuelo.html', {'error': 'Todos los campos son obligatorios'})

        # Crear un nuevo objeto Vuelo
        vuelo = Vuelo(
            Id_Empleado=Id_Empleado,
            Numero_Vuelo=Numero_Vuelo,
            Origen=Origen,
            Destino=Destino,
            Hora_llegada=Hora_llegada,
            Hora_Salida=Hora_Salida,
            Estado_Vuelo=Estado_Vuelo
        )

        # Guardar el vuelo en la base de datos
        vuelo.save()

        # Redirigir al usuario a la lista de vuelos después de guardar
        return redirect('Vuelo')

    return render(request, 'GestionarVuelo.html')

# Vista para editar un vuelo existente
def seleccionarVuelo(request, Id_Vuelo):
    vuelo = get_object_or_404(Vuelo, Id_Vuelo=Id_Vuelo)
    # Aquí puedes realizar cualquier lógica que necesites, como mostrar más detalles o realizar alguna acción adicional.
    return render(request, 'GestionarVuelo.html', {'vuelo': vuelo})

def editarVuelo(request, id):
    vuelo = get_object_or_404(Vuelo, Id_Vuelo=id)

    if request.method == 'POST':
        # Actualizar los datos del vuelo
        vuelo.Id_Empleado = request.POST.get('txtId_Empleado')
        vuelo.Numero_Vuelo = request.POST.get('txtNumero_Vuelo')
        vuelo.Origen = request.POST.get('txtOrigen')
        vuelo.Destino = request.POST.get('txtDestino')
        vuelo.Hora_llegada = request.POST.get('txtHora_llegada')
        vuelo.Hora_Salida = request.POST.get('txtHora_Salida')
        vuelo.Estado_Vuelo = request.POST.get('txtEstado_Vuelo')

        # Guardar los cambios
        vuelo.save()

        # Redirigir a la vista de inicio con un mensaje de éxito
        return render(request, 'editarVuelo.html', {
            'vuelo': vuelo,
            'mensaje_exito': '¡Vuelo actualizado exitosamente!'
        })

    return render(request, 'editarVuelo.html', {'vuelo': vuelo})
# Vista para borrar un vuelo específico
def borrarVuelo(request, Id_Vuelo):
    vuelo = get_object_or_404(Vuelo, Id_Vuelo=Id_Vuelo)

    if request.method == 'POST':
        # Borrar el vuelo
        vuelo.delete()
        return redirect('Vuelo')

    return render(request, 'BorrarVuelo.html', {'vuelo': vuelo})

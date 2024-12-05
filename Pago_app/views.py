from django.shortcuts import render, redirect, get_object_or_404
from .models import Pago

def inicio_vista(request):
    pagos = Pago.objects.all()  # Obtener todos los pagos almacenados
    return render(request, 'GestionarPago.html', {'pagos': pagos})

def registrarPago(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        Id_Pago = request.POST.get('txtId_Pago')
        Id_Pasagero = request.POST.get('txtId_Pasagero')
        Id_Empleado = request.POST.get('txtId_Empleado')
        Id_Vuelo = request.POST.get('txtId_Vuelo')
        Id_Boleto = request.POST.get('txtId_Boleto')
        Precio = request.POST.get('txtPrecio')
        Fecha_Pago = request.POST.get('txtFecha_Pago')
        Metodo_Pago = request.POST.get('txtMetodo_Pago')
        Estado = request.POST.get('txtEstado')

        # Validar si todos los campos están presentes
        if not (Id_Pago and Id_Pasagero and Id_Empleado and Id_Vuelo and Id_Boleto and Precio and Fecha_Pago and Metodo_Pago and Estado):
            return render(request, 'GestionarPago.html', {'error': 'Todos los campos son obligatorios'})

        # Crear un nuevo objeto Pago
        pago = Pago(
            Id_Pago=Id_Pago,
            Id_Pasagero=Id_Pasagero,
            Id_Empleado=Id_Empleado,
            Id_Vuelo=Id_Vuelo,
            Id_Boleto=Id_Boleto,
            Precio=Precio,
            Fecha_Pago=Fecha_Pago,
            Metodo_Pago=Metodo_Pago,
            Estado=Estado
        )

        # Guardar el pago en la base de datos
        pago.save()

        # Redirigir al usuario a la lista de pagos después de guardar
        return redirect('Pago')

    return render(request, 'GestionarPago.html')

# Seleccionar un pago (por ejemplo, para mostrar detalles)
def seleccionarPago(request, Id_Pago):
    pago = get_object_or_404(Pago, Id_Pago=Id_Pago)
    return render(request, 'GestionarPago.html', {'pago': pago})

# Editar un pago existente
def editarPago(request, Id_Pago):
    pago = get_object_or_404(Pago, Id_Pago=Id_Pago)
    if request.method == "POST":
        pago.Id_Pasagero = request.POST.get('txtId_Pasagero')
        pago.Id_Empleado = request.POST.get('txtId_Empleado')
        pago.Id_Vuelo = request.POST.get('txtId_Vuelo')
        pago.Id_Boleto = request.POST.get('txtId_Boleto')
        pago.Precio = request.POST.get('txtPrecio')
        pago.Fecha_Pago = request.POST.get('txtFecha_Pago')
        pago.Metodo_Pago = request.POST.get('txtMetodo_Pago')
        pago.Estado = request.POST.get('txtEstado')
        pago.save()
        return redirect('/')  # Redirigir a la vista principal después de actualizar

    return render(request, 'editarPago.html', {'pago': pago})

# Borrar un pago
def borrarPago(request, Id_Pago):
    pago = get_object_or_404(Pago, Id_Pago=Id_Pago)
    pago.delete()
    return redirect('Pago')  # Redirigir a la vista principal después de borrar

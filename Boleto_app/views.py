from django.shortcuts import render, redirect, get_object_or_404
from .models import Boleto

# Vista principal: Listar todos los boletos
def inicio_vista(request):
    if request.method == "POST":
        # Registrar un nuevo boleto desde el formulario
        id_boleto = request.POST.get('txtId_Boleto')
        id_reserva = request.POST.get('txtId_Reserva')
        numero_boleto = request.POST.get('txtNumero_Boleto')
        precio = request.POST.get('txtPrecio')
        fecha_emicion = request.POST.get('txtFecha_Emicion')
        estado_boleto = request.POST.get('txtEstado_Boleto')
        clase_servicio = request.POST.get('txtClase_Servicio')

        # Crear y guardar el nuevo boleto
        boleto = Boleto(
            Id_Boleto=id_boleto,
            Id_Reserva=id_reserva,
            Numero_Boleto=numero_boleto,
            Precio=precio,
            Fecha_Emicion=fecha_emicion,
            Estado_Boleto=estado_boleto,
            Clase_Servicio=clase_servicio
        )
        boleto.save()
        return redirect('Boleto')  # Redirigir a la vista principal después de guardar

    # Listar todos los boletos
    boletos = Boleto.objects.all()
    return render(request, 'GestionarBoleto.html', {'boletos': boletos})

# Registrar un nuevo boleto
def registrarBoleto(request):
    if request.method == "POST":
        id_boleto = request.POST.get('txtId_Boleto')
        id_reserva = request.POST.get('txtId_Reserva')
        numero_boleto = request.POST.get('txtNumero_Boleto')
        precio = request.POST.get('txtPrecio')
        fecha_emicion = request.POST.get('txtFecha_Emicion')
        estado_boleto = request.POST.get('txtEstado_Boleto')
        clase_servicio = request.POST.get('txtClase_Servicio')

        boleto = Boleto(
            Id_Boleto=id_boleto,
            Id_Reserva=id_reserva,
            Numero_Boleto=numero_boleto,
            Precio=precio,
            Fecha_Emicion=fecha_emicion,
            Estado_Boleto=estado_boleto,
            Clase_Servicio=clase_servicio,
        )
        boleto.save()
        return redirect('Boleto')
    return render(request, 'GestionarBoleto.html')

# Seleccionar un boleto (por ejemplo, para mostrar detalles)
def seleccionarBoleto(request, Id_Boleto):
    boleto = get_object_or_404(Boleto, Id_Boleto=Id_Boleto)
    return render(request, 'GestionarBoleto.html', {'boleto': boleto})

# Editar un boleto existente
def editarBoleto(request, Id_Boleto):
    boleto = get_object_or_404(Boleto, Id_Boleto=Id_Boleto)
    if request.method == "POST":
        boleto.Id_Reserva = request.POST.get('txtId_Reserva')
        boleto.Numero_Boleto = request.POST.get('txtNumero_Boleto')
        boleto.Precio = request.POST.get('txtPrecio')
        boleto.Fecha_Emicion = request.POST.get('txtFecha_Emicion')
        boleto.Estado_Boleto = request.POST.get('txtEstado_Boleto')
        boleto.Clase_Servicio = request.POST.get('txtClase_Servicio')
        boleto.save()
        return redirect('/')
    return render(request, 'editarBoleto.html', {'boleto': boleto})

# Borrar un boleto
def borrarBoleto(request, Id_Boleto):
    boleto = get_object_or_404(Boleto, Id_Boleto=Id_Boleto)
    boleto.delete()
    return redirect('Boleto')

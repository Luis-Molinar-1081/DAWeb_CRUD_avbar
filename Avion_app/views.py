from django.shortcuts import render, redirect
from .models import Avion

# Vista para la página de inicio
def inicio_vista(request):
    ListadoAvion = Avion.objects.all()
    return render(request, "GestionarAvion.html", {"losAviones": ListadoAvion})

# Vista para registrar aviones
def registrarAvion(request):
    if request.method == 'POST':
        capacidad_asientos = int(request.POST.get('numCapacidad_Asientos'))
        capacidad_carga = int(request.POST.get('numCapacidad_Carga'))

        # Validar los valores
        if capacidad_asientos > 500 or capacidad_carga > 5000000:
            return render(request, 'GestionarAvion.html', {
                "error": "Los valores exceden el límite permitido.",
            })

        # Guardar el nuevo avión
        nuevo_avion = Avion(
            Id_Avion=request.POST.get('txtId_Avion'),
            Modelo=request.POST.get('txtModelo'),
            Aerolinea=request.POST.get('txtAerolinea'),
            Capacidad_Asientos=capacidad_asientos,
            Capacidad_Carga=capacidad_carga,
            Año_Fabricacion=request.POST.get('txtAño_Fabricacion'),
            Estado_Avion=request.POST.get('txtEstado_Avion'),
        )
        nuevo_avion.save()
        return redirect('Avion')

    return render(request, 'GestionarAvion.html')

def seleccionarAvion(request, Id_Avion):
    avion = Avion.objects.get(Id_Avion=Id_Avion)  # Usar 'avion' en minúsculas
    return render(request, "editarAvion.html", {"misAviones": avion})


def editarAvion(request):
    if request.method == 'POST':
        Id_Avion = request.POST['txtId_Avion']
        try:
            avion = Avion.objects.get(Id_Avion=Id_Avion)  # Busca el avión por su ID
            avion.Modelo = request.POST['txtModelo']
            avion.Aerolinea = request.POST['txtAerolinea']
            avion.Capacidad_Asientos = int(request.POST['numCapacidad_Asientos'])
            avion.Capacidad_Carga = int(request.POST['numCapacidad_Carga'])
            avion.Año_Fabricacion = request.POST['txtAño_Fabricacion']
            avion.Estado_Avion = request.POST['txtEstado_Avion']
            avion.save()  # Guarda los cambios
            return redirect('Avion')
        except Avion.DoesNotExist:
            return render(request, 'error.html', {"mensaje": "El avión no existe."})
    return redirect('Avion')  # Redirige si no es una solicitud POST

def borrarAvion(request, Id_Avion):
    try:
        # Busca el avión usando el modelo `Avion`
        avion = Avion.objects.get(Id_Avion=Id_Avion)
        avion.delete()  # Elimina el avión
        return redirect("Avion")  # Redirige a la vista principal
    except Avion.DoesNotExist:
        # Maneja el caso donde no existe el avión
        return render(request, "error.html", {"mensaje": "El avión no existe"})


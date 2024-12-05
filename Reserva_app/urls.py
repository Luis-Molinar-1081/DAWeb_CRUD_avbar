from django.urls import path
from Reserva_app import views

urlpatterns = [
    path('Reserva', views.inicio_vista, name='Reserva'),
    path('registrarReserva/', views.registrarReserva, name='registrarReserva'),
    path('seleccionarReserva/<int:Id_Reserva>/', views.seleccionarReserva, name='seleccionarReserva'),
     path('editarReserva/<int:id>/', views.editarReserva, name='editarReserva'),
    path('borrarReserva/<str:Id_Reserva>/', views.borrarReserva, name='borrarReserva'),
]
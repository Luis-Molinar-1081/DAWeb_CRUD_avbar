from django.urls import path
from Pago_app import views

urlpatterns = [
    path('Pago', views.inicio_vista, name='Pago'),
    path('registrarPago/', views.registrarPago, name='registrarPago'),  # Vista para registrar
    path('seleccionarPago/<str:Id_Pago>/', views.seleccionarPago, name='seleccionarPago'),  # Vista para seleccionar
    path('editarPago/<str:Id_Pago>/', views.editarPago, name='editarPago'),  # Vista para editar
    path('borrarPago/<str:Id_Pago>/', views.borrarPago, name='borrarPago'),  # Vista para borrar
]

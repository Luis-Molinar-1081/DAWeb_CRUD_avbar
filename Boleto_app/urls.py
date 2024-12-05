from django.urls import path
from Boleto_app import views

urlpatterns = [
    path('Boleto', views.inicio_vista, name='Boleto'),
    path('registrarBoleto/', views.registrarBoleto, name='registrarBoleto'),  # Vista para registrar
    path('seleccionarBoleto/<str:Id_Boleto>/', views.seleccionarBoleto, name='seleccionarBoleto'),  # Vista para seleccionar
    path('editarBoleto/<str:Id_Boleto>/', views.editarBoleto, name='editarBoleto'),  # Vista para editar
    path('borrarBoleto/<str:Id_Boleto>/', views.borrarBoleto, name='borrarBoleto'),  # Vista para borrar
]

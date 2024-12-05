from django.urls import path
from Pasajero_app import views

urlpatterns = [
    path("Pasajero",views.inicio_vista,name="Pasajero"),
    path('registrarPasagero/', views.registrarPasagero, name='registrarPasagero'),
    path("seleccionarPasagero/<Id_Pasagero>",views.seleccionarPasagero,name="seleccionarPasagero"),
    path("editarPasagero/",views.editarPasagero,name="editarPasagero"),
    path("borrarPasagero/<Id_Pasagero>", views.borrarPasagero, name="borrarPasagero"),
]

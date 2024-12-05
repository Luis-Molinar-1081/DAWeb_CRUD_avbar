from django.urls import path
from Avion_app import views

urlpatterns = [
    path("Avion",views.inicio_vista,name="Avion"),
    path('registrarAvion/', views.registrarAvion, name='registrarAvion'),
    path("seleccionarAvion/<Id_Avion>",views.seleccionarAvion,name="seleccionarAvion"),
    path("editarAvion/",views.editarAvion,name="editarAvion"),
    path("borrarAvion/<Id_Avion>", views.borrarAvion, name="borrarAvion"),
]

from django.urls import path
from Vuelo_app import views

from django.urls import path
from . import views

urlpatterns = [
    path('Vuelo', views.inicio_vista, name='Vuelo'),
    path('registrar_vuelo/', views.registrarVuelo, name='registrarVuelo'),
    path('editarVuelo/<int:id>/', views.editarVuelo, name='editarVuelos'),
    path('borrarVuelo/<int:Id_Vuelo>/', views.borrarVuelo, name='borrarVuelos'),
]

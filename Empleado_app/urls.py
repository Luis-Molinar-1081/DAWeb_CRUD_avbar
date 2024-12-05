from django.urls import path
from Empleado_app import views

urlpatterns = [
    path('Empleado', views.inicio_vista, name='Empleado'),
    path('registrarEmpleado/', views.registrarEmpleado, name='registrarEmpleado'),
    path('seleccionarEmpleado/<int:Id_Empleado>/', views.seleccionarEmpleado, name='seleccionarEmpleado'),
    path('editarEmpleado/<int:Id_Empleado>/', views.editarEmpleado, name='editarEmpleado'),
    path('borrarEmpleado/<str:Id_Empleado>/', views.borrarEmpleado, name='borrarEmpleado'),
]

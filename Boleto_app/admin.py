from django.contrib import admin
from .models import Boleto

# Registrar el modelo Boleto para que aparezca en el admin
admin.site.register(Boleto)

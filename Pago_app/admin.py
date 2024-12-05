from django.contrib import admin
from .models import Pago

# Registrar el modelo Pago para que aparezca en el admin
admin.site.register(Pago)

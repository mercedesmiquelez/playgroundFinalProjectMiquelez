from django.contrib import admin
from .models import Servicio, Vendedor, Comprador, Producto, Usuario

admin.site.register(Servicio)
admin.site.register(Vendedor)
admin.site.register(Comprador)
admin.site.register(Producto)
admin.site.register(Usuario)
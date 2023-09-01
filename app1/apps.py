from django.apps import AppConfig

class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'

    def ready(self):
        # Importa tus modelos aquí para asegurarte de que las aplicaciones estén cargadas
        from .models import Servicio, Vendedor, Comprador, Producto, Usuario
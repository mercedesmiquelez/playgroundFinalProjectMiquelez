from email.mime import image
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Comprador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Descripcion: {self.descripcion} - Cantidad: {self.cantidad}"


class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(default='correo@example.com')
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email}"

class Servicio(models.Model):
    title = models.CharField(max_length=200) 
    subtitle =  models.CharField(max_length=200)
    descripcion = models.TextField()
    autor = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="servicios", null=True)
    
    def __str__(self) -> str:
        return f"Titulo: {self.title} - Subtitulo: {self.subtitle} - Descripcion: {self.descripcion} - Autor: {self.autor} - Imagen: {self.imagen}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # imagen = models.ImageField(upload_to="posts", null=True)

    def __str__(self):
        return f"Titulo: {self.title} - Subtitulo: {self.subtitle} - Comentario: {self.content} - Autor: {self.created_at}"
    
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='usuarios', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
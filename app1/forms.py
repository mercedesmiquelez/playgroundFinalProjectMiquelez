from dataclasses import field
from django import forms
from .models import Servicio, Vendedor, Comprador, Post, Producto
from django.contrib.auth.forms import UserCreationForm, UserModel, UserChangeForm
# from django.contrib.auth import UserModel
# from django.contrib.auth.models import UserModel

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'

class CompradorForm(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = '__all__'
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoSearchForm(forms.Form):
    nombre = forms.CharField(required=False)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = UserCreationForm.Meta.fields 
        
class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    imagen = forms.ImageField(label="Usuario", required=False)
    
    class Meta:
        model = UserModel
        fields = ['email', 'last_name', 'first_name', 'imagen']

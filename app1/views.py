from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Producto, Servicio, Vendedor, Comprador, Post
from .forms import ServicioForm, VendedorForm, CompradorForm, ProductoSearchForm, PostForm, CustomUserCreationForm, UserEditForm, ProductoForm, ServicioForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    return render(request, 'index.html')

def aboutme(request):
    return render(request, 'aboutme.html')

# Vistas para el modelo Producto
class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'
    context_object_name = 'productos'

def producto_create(request):
    if request.method == 'POST':
        mi_formulario = ProductoForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
        return render(request, 'index.html')
    else:
        mi_formulario = ProductoForm()
        return render(request, 'producto_create.html', {'mi_formulario': mi_formulario})


class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicio_list.html'
    context_object_name = 'servicios'
    
def servicio_form(request):
    if request.method == 'POST':
        mi_formulario = ServicioForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
        return render(request, 'index.html')
    else:
        mi_formulario = ServicioForm()
        return render(request, 'servicio_form.html', {'mi_formulario': mi_formulario})

# Vistas para el modelo Vendedor
class VendedorCreateView(CreateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'vendedor_form.html'
    success_url = reverse_lazy('app1:index')

class VendedorListView(ListView):
    model = Vendedor
    template_name = 'vendedor_list.html'
    context_object_name = 'vendedores'

# Vistas para el modelo Comprador
# class CompradorCreateView(CreateView):
#     model = Comprador
#     form_class = CompradorForm
#     template_name = 'comprador_form.html'
#     success_url = reverse_lazy('app1:index')

class CompradorListView(ListView):
    model = Comprador
    template_name = 'comprador_list.html'
    context_object_name = 'compradores'
    
def comprador_form(request):
    if request.method == 'POST':
        mi_formulario = CompradorForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
        return render(request, 'index.html')
    else:
        mi_formulario = ProductoForm()
        return render(request, 'comprador_form.html', {'mi_formulario': mi_formulario})
    
class CompradorUpdateView(UpdateView):
    model = Comprador
    form_class = CompradorForm
    template_name = 'update_comprador.html'
    success_url = reverse_lazy('app1:comprador_list')
    
class CompradorDeleteView(DeleteView):
    model = Comprador
    template_name = 'delete_comprador.html'
    success_url = reverse_lazy('app1:comprador_list')

# Vista para buscar productos por descripcion
def buscar_productos(request):
    producto = []
    form = ProductoSearchForm(request.GET)

    if form.is_valid():
        descripcion = form.cleaned_data.get('descripcion')

        if descripcion:
            producto = Producto.objects.filter(nombre__icontains=descripcion)

    return render(request, 'buscar_productos.html', {'form': form, 'producto': producto})

# Vistas para el modelo Producto
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['descripcion', 'cantidad']
    template_name = 'producto_update.html'
    success_url = reverse_lazy('app1:producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('app1:producto_list')

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('app1:post_list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('app1:post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('app1:post_list')

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('app1:login')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            return redirect('app1:index')  
        return response

class CustomLogoutView(LogoutView):
    next_page = 'app1:login'
    
    
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()
                
            miFormulario.save()
            return render(request, "app1/index.html")
        
    else:
        miFormulario = UserEditForm(instance=request.user)
    return render(request, "app1/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "app1/cambiar_contrasenia.html"
    success_url = reverse_lazy('EditarPerfil')

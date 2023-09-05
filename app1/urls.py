from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('aboutme/', views.aboutme, name='aboutme'),  
    path('producto_list/', views.ProductoListView.as_view(), name='producto_list'),
    path('producto_create/', views.producto_create, name='producto_create'),
    path('servicio_list/', views.ServicioListView.as_view(), name='servicio_list'),
    path('servicio_form/', views.servicio_form, name='servicio_form'),
    path('vendedor_list/', views.VendedorListView.as_view(), name='vendedor_list'),
    path('comprador_list/', views.CompradorListView.as_view(), name='comprador_list'),
    path('vendedor_form/', views.vendedor_form, name='vendedor_form'),
    path('comprador_form/', views.comprador_form, name='comprador_form'),
    path('buscar-por-nombre/', views.buscar_productos, name='buscar_productos'),
    path('producto_update/<int:pk>/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('producto_delete/<int:pk>/', views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail_post'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
    path('CambiarContrasenia/', views.CambiarContrasenia.as_view(), name="CambiarContrasenia"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

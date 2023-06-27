from django.urls import path

from apps.Tienda import admin

from .import views
from .views import agregar_producto, home, registro


urlpatterns = [
   # path('admin/', admin.site.urls),
    
    #Producto
    path('home',views.cargarInicio),
    path('agregarProducto',views.cargarAgregarProducto),
    path('agregarProductoForm',views.agregarProducto),
    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProducto',views.editarProducto),
    path('eliminarProducto/<codigo_producto>',views.eliminarProducto),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    
    #Carrito
    #path('carrito',views.Carrito),
    #path('carrito/', views.ver_carrito, name='ver_carrito'),
    #path('carrito/agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    #path('carrito/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    #path('admin/', admin.site.urls),
    #path('', Tienda, name="Tienda"),

    #Usuario
    #path('agregarUsuario/',views.cargarAgregarUsuario),
    #path('agregarUsuarioForm', views.agregarUsuario),
    #path('editarUsuario/<nombre>', views.cargarEditarUsuario),
    #path('listaUsuarios', views.lista_usuarios),
    #path('editarUsuario', views.editarUsuario),
    #path('eliminrUsuario/<nombre>', views.eliminarUsuario),


    #Login
    path('', home, name="home"),

    #Registro
    path('registro/', registro, name="registro"),

    #Contacto
    path('contacto', views.contacto)
]

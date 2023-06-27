import json
import os
from django.shortcuts import render, redirect
from .models import Producto, Carrito, Categoria
from .forms import ProductoForm, CustomUserCreationForm, ContactoForm
from django.conf import settings
from django.contrib.auth import authenticate, login


from django.http import HttpResponse

# Create your views here.

#Contacto
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'contacto.html',data)



#Registro
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            print("Te has registrado correctamente")
            #Redirigir al home
            return redirect(to="home")
        data["from"] = formulario

    return render(request, 'registration/registro.html', data)

#Login
def home(request):
    return render(request, 'inicio.html')
    
def cargarInicio(request):
    productos = Producto.objects.all()
    cate_producto_jardineria = Producto.objects.filter(categoriaId = 1) 
    cate_producto_planta = Producto.objects.filter(categoriaId = 2) 
    return render(request,"inicio.html",{"producto":productos,"cate_planta":cate_producto_planta,"cate_jardineria": cate_producto_jardineria})

#Producto
def agregar_producto(request):

    data = {
        'form': ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'agregar.html', data)

def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"agregarProductos.html",{"cate":categorias,"prod":productos})

def agregarProducto(request):
    #print("AGREGAR PRODUCTOS", request.POST)

    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_imagen = request.FILES['txtImagen']
    
    Producto.objects.create(sku = v_sku, nombre = v_nombre, precio = v_precio,stock = v_stock, descripcion = v_descripcion, imagenUrl=v_imagen,categoriaId = v_categoria)

def cargarEditarProducto(request,sku):
    prod = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()
    return render(request,"editarProducto.html",{"prod":prod, "cate":categorias})

def editarProducto(request):
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']

    try:
        v_imagen = request.FILES['txtImagen']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagenUrl))
        os.remove(ruta_imagen)
    except:
        v_imagen = productoBD.imagenUrl

    productoBD.nombre = v_nombre
    productoBD.precio = v_precio
    productoBD.stock = v_stock
    productoBD.descripcion = v_descripcion
    productoBD.categoriaId = v_categoria
    productoBD.imagenUrl = v_imagen
    
    productoBD.save()

    return redirect('/agregarProducto')

def eliminarProducto(request,codigo_producto):
    producto = Producto.objects.get(sku = codigo_producto)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagenUrl))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregarProducto')

# Crear un nuevo carrito
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('apps:Tienda')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('apps:Tienda')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('apps:Tienda')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('apps:Tienda')
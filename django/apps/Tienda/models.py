from django.db import models


# Create your models here.
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=22)

    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.id_categoria , self.nombre_categoria)


class Producto(models.Model):
    sku = models.CharField(primary_key=True,max_length=15)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=120)
    imagenUrl = models.ImageField(upload_to="imagenesProducto")
    categoriaId = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Producto N° {0} - Stock {1} - Precio {2} - fecha {3}"
        return txt.format(self.sku,self.stock,self.precio,self.fecha)
    


class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=100)

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
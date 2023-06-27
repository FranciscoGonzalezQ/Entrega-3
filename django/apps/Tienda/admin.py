from django.contrib import admin
from . import models
from .models import Contacto
# Register your models here.

admin.site.register(models.Producto)
admin.site.register(models.Categoria)
admin.site.register(Contacto)
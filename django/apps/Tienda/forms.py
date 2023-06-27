from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Producto, Contacto


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"first_name", "last_name", "password1", "password2"]


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

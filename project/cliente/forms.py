from django import forms
from .models import Cliente, Nombre, Telefono, Email

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = []

class NombreForm(forms.ModelForm):
    class Meta:
        model = Nombre
        fields = ['nombre']

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['telefono']

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']
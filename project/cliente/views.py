from django.shortcuts import render

from . import models

def home(request):
    nombre_cliente = models.cliente.objects.all()
    context = {"Clientes": nombre_cliente}
    return render(request, "cliente/index.html", context)
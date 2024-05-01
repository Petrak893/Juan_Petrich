from django.shortcuts import render

from . import models

def home(request):
    query = models.Cliente.objects.all()
    context = {"Clientes": query}
    return render(request, "cliente/index.html", context)
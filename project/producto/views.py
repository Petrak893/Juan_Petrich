from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    if "consulta" in request.GET:
        consulta = request.GET["consulta"]
        productos = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
    else:
        productos = models.ProductoCategoria.objects.all()

    context = {"productos": productos}
    return render(request, "producto/index.html", context)

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else: # request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", context={"form": form})

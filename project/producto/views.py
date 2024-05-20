from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . import models, forms

def home(request):
    return render(request, "producto/index.html")

def productocategoria_list(request):
    if "consulta" in request.GET:
        consulta = request.GET["consulta"]
        productos = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
    else:
        productos = models.ProductoCategoria.objects.all()

    context = {"productos": productos}
    return render(request, "producto/productocategoria_list.html", context)

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else: # request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", context={"form": form})

def productocategoria_detail(request, pk):
    query = models.ProductoCategoria.objects.get(id=pk)
    return render(request, "pproducto/productocategoria_detail.html"), {"producto": query}

def productocategoria_update(request, pk:int):
    query = models.ProductoCategoria.objects.get(id=pk)
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else: # request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_update.html", context={"form": form})

def productocategoria_delete(request, pk:int):
    query = models.ProductoCategoria.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto:productocategoria_list")
    return render(request, "producto/productocategoria_delete.html")
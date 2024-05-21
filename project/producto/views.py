from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
def home(request):
    return render(request, "producto/index.html")


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(nombre__incontains=consulta)
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list

class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:home")

class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
   

class ProductoCategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoList(ListView):
    model = models.Producto
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__incontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:home")

class ProductoDetail(DetailView):
    model = models.Producto
   

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
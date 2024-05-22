from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
def home(request):
    return render(request, "personaje/index.html")


class NivelMutanteList(ListView):
    model = models.NivelMutante
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.NivelMutante.objects.filter(nombre__incontains=consulta)
        else:
            object_list = models.NivelMutante.objects.all()
        return object_list

class NivelMutanteCreate(LoginRequiredMixin, CreateView):
    model = models.NivelMutante
    form_class = forms.NivelMutanteForm
    success_url = reverse_lazy("personaje:home")

class NivelMutanteDetail(DetailView):
    model = models.NivelMutante
   

class NivelMutanteUpdate(LoginRequiredMixin, UpdateView):
    model = models.NivelMutante
    form_class = forms.NivelMutanteForm
    success_url = reverse_lazy("personaje:nivelmutante_list")

class NivelMutanteDelete(LoginRequiredMixin, DeleteView):
    model = models.NivelMutante
    success_url = reverse_lazy("personaje:nivelmutante_list")

class PersonajeList(ListView):
    model = models.Personaje
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Personaje.objects.filter(nombre__incontains=consulta)
        else:
            object_list = models.Personaje.objects.all()
        return object_list

class PersonajeCreate(LoginRequiredMixin, CreateView):
    model = models.Personaje
    form_class = forms.PersonajeForm
    success_url = reverse_lazy("personaje:home")

class PersonajeDetail(DetailView):
    model = models.Personaje
   

class PersonajeUpdate(LoginRequiredMixin, UpdateView):
    model = models.Personaje
    form_class = forms.PersonajeForm
    success_url = reverse_lazy("personaje:personaje_list")

class PersonajeDelete(LoginRequiredMixin, DeleteView):
    model = models.Personaje
    success_url = reverse_lazy("personaje:personaje_list")
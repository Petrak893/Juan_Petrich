from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy

def home(request):
    return render(request, "autores/index.html")

class AutorCreateView(CreateView):
    model = models.Autor
    form_class = forms.AutorForm
    template_name = 'autores/autores_form.html'
    success_url = reverse_lazy('autores:autores_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['files'] = self.request.FILES
        return kwargs


class AutorListView(ListView):
    model = models.Autor
    template_name = 'autores/autores_list.html'

class AutorDetailView(DetailView):
    model = models.Autor
    template_name = 'autores/autores_detail.html'

class AutorUpdateView(UpdateView):
    model = models.Autor
    form_class = forms.AutorForm
    template_name = 'autores/autores_form.html'
    success_url = reverse_lazy('autores:autores_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['files'] = self.request.FILES
        return kwargs


class AutorDeleteView(DeleteView):
    model = models.Autor
    template_name = 'autores/autores_confirm_delete.html'
    success_url = reverse_lazy('autores:autores_list')
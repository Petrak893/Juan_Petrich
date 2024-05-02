from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm 

def home(request):
    if "consulta" in request.GET:
        consulta = request.GET["consulta"]
        clientes = Cliente.objects.filter(nombre__nombre__icontains=consulta) 
    else:
        clientes = Cliente.objects.all()

    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)

def cliente_create(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente = cliente_form.save()
            return redirect("cliente:home")
        else:
            print(cliente_form.errors)
    else:
        cliente_form = ClienteForm()

    return render(request, 'cliente/cliente_create.html', context={'cliente_form': cliente_form})
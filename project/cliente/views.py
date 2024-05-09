from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm, NombreForm, TelefonoForm, EmailForm

def home(request):
    if "consulta" in request.GET:
        consulta = request.GET["consulta"]
        clientes = Cliente.objects.filter(nombre__icontains=consulta)
    else:
        clientes = Cliente.objects.all()

    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:home')
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_create.html', {'form': form})
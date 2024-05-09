from django.shortcuts import render, redirect
from .models import Cliente, Nombre, Telefono, Email
from .forms import ClienteForm, NombreForm, TelefonoForm, EmailForm

def home(request):
    if "consulta" in request.GET:
        consulta = request.GET["consulta"]
        clientes = Cliente.objects.filter(nombre__nombre__icontains=consulta)
    else:
        clientes = Cliente.objects.all()

    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)

def crear_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        nombre_form = NombreForm(request.POST)
        telefono_form = TelefonoForm(request.POST)
        email_form = EmailForm(request.POST)
        if cliente_form.is_valid() and nombre_form.is_valid() and telefono_form.is_valid() and email_form.is_valid():
            nombre = nombre_form.save()
            telefono = telefono_form.save()
            email = email_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.nombre = nombre
            cliente.telefono = telefono
            cliente.email = email
            cliente.save()
            return redirect('cliente:home')
    else:
        cliente_form = ClienteForm()
        nombre_form = NombreForm()
        telefono_form = TelefonoForm()
        email_form = EmailForm()
    return render(request, 'cliente/cliente_create.html', {'cliente_form': cliente_form, 'nombre_form': nombre_form, 'telefono_form': telefono_form, 'email_form': email_form})
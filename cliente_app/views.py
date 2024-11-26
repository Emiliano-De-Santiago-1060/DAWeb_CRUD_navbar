from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.

def inicio_vistaCliente(request):
    losclientes=Cliente.objects.all()

    return render(request, "gestionarCliente.html", {"misclientes":losclientes})

def registrarCliente(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    fecha=request.POST["datefecha"]
    correo=request.POST["txtcorreo"]
    
    guardarproveedor=Cliente.objects.create(codigo=codigo, nombre=nombre, direccion=direccion, telefono=telefono, fecha=fecha, correo=correo)
    return redirect("cliente")

def seleccionarCliente(request, codigo):
    cliente=Cliente.objects.get(codigo=codigo)
    return render(request, "editarCliente.html", {"misclientes":cliente})

def borrarCliente(request, codigo):
    cliente=Cliente.objects.get(codigo=codigo)
    cliente.delete()
    return redirect("cliente")

def editarCliente(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    fecha=request.POST["datefecha"]
    correo=request.POST["txtcorreo"]
    
    cliente=Cliente.objects.get(codigo=codigo)
    cliente.nombre=nombre
    cliente.direccion=direccion
    cliente.telefono=telefono
    cliente.fecha=fecha
    cliente.correo=correo
    cliente.save()
    return redirect("cliente")
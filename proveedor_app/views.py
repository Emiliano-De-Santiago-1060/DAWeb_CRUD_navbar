from django.shortcuts import render, redirect
from .models import Proveedor
# Create your views here.

def inicio_vistaProveedor(request):
    losproveedores=Proveedor.objects.all()

    return render(request, "gestionarProveedor.html", {"misproveedores":losproveedores})

def registrarProveedor(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    giro=request.POST["txtgiro"]

    guardarproveedor=Proveedor.objects.create(codigo=codigo, nombre=nombre, direccion=direccion, telefono=telefono, giro=giro)
    return redirect("/")

def seleccionarProveedor(request, codigo):
    proveedor=Proveedor.objects.get(codigo=codigo)
    return render(request, "editarProveedor.html", {"misproveedores":proveedor})

def borrarProveedor(request, codigo):
    proveedor=Proveedor.objects.get(codigo=codigo)
    proveedor.delete()
    return redirect("/")

def editarProveedor(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    giro=request.POST["txtgiro"]
    proveedor=Proveedor.objects.get(codigo=codigo)
    proveedor.nombre=nombre
    proveedor.direccion=direccion
    proveedor.telefono=telefono
    proveedor.giro=giro
    proveedor.save()
    return redirect("/")
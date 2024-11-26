from django.shortcuts import render, redirect
from .models import Personal
# Create your views here.

def inicio_vistaPersonal(request):
    lospersonales=Personal.objects.all()

    return render(request, "gestionarPersonal.html", {"mispersonales":lospersonales})

def registrarPersonal(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    cargo=request.POST["txtcargo"]
    sueldo=request.POST["numsueldo"]
    
    guardarpersonal=Personal.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, cargo=cargo, sueldo=sueldo)
    return redirect("/")

def seleccionarPersonal(request, codigo):
    personal=Personal.objects.get(codigo=codigo)
    return render(request, "editarPersonal.html", {"mispersonales":personal})

def borrarPersonal(request, codigo):
    personal=Personal.objects.get(codigo=codigo)
    personal.delete()
    return redirect("/")

def editarPersonal(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    cargo=request.POST["txtcargo"]
    sueldo=request.POST["numsueldo"]
    
    
    personal=Personal.objects.get(codigo=codigo)
    personal.nombre=nombre
    personal.apellido=apellido
    personal.direccion=direccion
    personal.telefono=telefono
    personal.cargo=cargo
    personal.sueldo=sueldo
    personal.save()
    return redirect("/")
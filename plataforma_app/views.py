from django.shortcuts import render, redirect
from .models import Plataforma
# Create your views here.

def inicio_vistaPlataforma(request):
    losplataformas=Plataforma.objects.all()

    return render(request, "gestionarPlataforma.html", {"misplataformas":losplataformas})

def registrarPlataforma(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    tipo=request.POST["txttipo"]
    encargado=request.POST["txtencargado"]
    servicio=request.POST["txtservicio"]
    ganancias=request.POST["numganancias"]



    
    guardarplataforma=Plataforma.objects.create(codigo=codigo, nombre=nombre, tipo=tipo, encargado=encargado, servicio=servicio, ganancias=ganancias)
    return redirect("/")

def seleccionarPlataforma(request, codigo):
    plataforma=Plataforma.objects.get(codigo=codigo)
    return render(request, "editarPlataforma.html", {"misplataformas":plataforma})

def borrarPlataforma(request, codigo):
    plataforma=Plataforma.objects.get(codigo=codigo)
    plataforma.delete()
    return redirect("/")

def editarPlataforma(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    tipo=request.POST["txttipo"]
    encargado=request.POST["txtencargado"]
    servicio=request.POST["txtservicio"]
    ganancias=request.POST["numganancias"]
    
    plataforma=Plataforma.objects.get(codigo=codigo)
    plataforma.nombre=nombre
    plataforma.tipo=tipo
    plataforma.encargado=encargado
    plataforma.servicio=servicio
    plataforma.ganancias=ganancias
    plataforma.save()
    return redirect("/")
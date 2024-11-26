from django.shortcuts import render, redirect
from .models import Venta
# Create your views here.

def inicio_vistaVenta(request):
    losventas=Venta.objects.all()

    return render(request, "gestionarVenta.html", {"misventas":losventas})

def registrarVenta(request):
    codigo=request.POST["txtcodigo"]
    codigoper=request.POST["txtcodigoper"]
    codigopro=request.POST["txtcodigopro"]
    codigocli=request.POST["txtcodigocli"]
    fecha=request.POST["datefecha"]
    cantidad=request.POST["numcantidad"]
    total=request.POST["numtotal"]

    guardarventa=Venta.objects.create(codigo=codigo, codigoper=codigoper, codigopro=codigopro, codigocli=codigocli, fecha=fecha, cantidad=cantidad, total=total)
    return redirect("/")

def seleccionarVenta(request, codigo):
    venta=Venta.objects.get(codigo=codigo)
    return render(request, "editarVenta.html", {"misventas":venta})

def borrarVenta(request, codigo):
    venta=Venta.objects.get(codigo=codigo)
    venta.delete()
    return redirect("/")

def editarVenta(request):
    codigo=request.POST["txtcodigo"]
    codigoper=request.POST["txtcodigoper"]
    codigopro=request.POST["txtcodigopro"]
    codigocli=request.POST["txtcodigocli"]
    fecha=request.POST["datefecha"]
    cantidad=request.POST["numcantidad"]
    total=request.POST["numtotal"]
    
    venta=Venta.objects.get(codigo=codigo)
    venta.codigoper=codigoper
    venta.codigopro=codigopro
    venta.codigocli=codigocli
    venta.fecha=fecha
    venta.cantidad=cantidad
    venta.total=total
    venta.save()
    return redirect("/")
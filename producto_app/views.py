from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.

def inicio_vistaProducto(request):
    losproductos=Producto.objects.all()

    return render(request, "gestionarProducto.html", {"misproductos":losproductos})

def registrarProducto(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    precio=request.POST["numprecio"]
    cantidad=request.POST["numcantidad"]
    descripcion=request.POST["txtdescripcion"]
    estado=request.POST["txtestado"]
    caducidad=request.POST["datecaducidad"]



    
    guardarproducto=Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, cantidad=cantidad, descripcion=descripcion, estado=estado, caducidad=caducidad)
    return redirect("/")

def seleccionarProducto(request, codigo):
    producto=Producto.objects.get(codigo=codigo)
    return render(request, "editarProducto.html", {"misproductos":producto})

def borrarProducto(request, codigo):
    producto=Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect("/")

def editarProducto(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    precio=request.POST["numprecio"]
    cantidad=request.POST["numcantidad"]
    descripcion=request.POST["txtdescripcion"]
    estado=request.POST["txtestado"]
    caducidad=request.POST["datecaducidad"]
    producto=Producto.objects.get(codigo=codigo)
    producto.nombre=nombre
    producto.precio=precio
    producto.cantidad=cantidad
    producto.descripcion=descripcion
    producto.estado=estado
    producto.caducidad=caducidad
    producto.save()
    return redirect("/")
from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    precio=models.PositiveIntegerField()
    cantidad=models.PositiveIntegerField()
    descripcion=models.TextField(max_length=300)
    estado=models.CharField(max_length=100)
    caducidad=models.DateField(max_length=100)



    def __str__(self):
        return self.nombre
    
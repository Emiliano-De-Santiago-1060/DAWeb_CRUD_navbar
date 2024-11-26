from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    direccion=models.TextField(max_length=300)
    telefono=models.TextField(max_length=300)
    giro=models.TextField(max_length=300)



    def __str__(self):
        return self.nombre
    
from django.db import models

# Create your models here.
class Personal(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.TextField(max_length=300)
    direccion=models.TextField(max_length=100)
    telefono=models.TextField(max_length=100)
    cargo=models.TextField(max_length=100)
    sueldo=models.FloatField(max_length=100)





    def __str__(self):
        return self.nombre
    
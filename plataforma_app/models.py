from django.db import models

# Create your models here.
class Plataforma(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    tipo=models.TextField(max_length=300)
    encargado=models.TextField(max_length=300)
    servicio=models.TextField(max_length=300)
    ganancias=models.FloatField(max_length=100)


    def __str__(self):
        return self.nombre
    
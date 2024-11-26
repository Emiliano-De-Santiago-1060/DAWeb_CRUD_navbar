from django.db import models

# Create your models here.
class Venta(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    codigoper=models.CharField(max_length=6)
    codigopro=models.CharField(max_length=6)
    codigocli=models.CharField(max_length=6)
    fecha=models.DateField(max_length=100)
    cantidad=models.CharField(max_length=6)
    total=models.FloatField(max_length=100)

    def __str__(self):
        return self.codigo
    
from django.db import models

# Create your models here.

class Oferta(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_vencimiento = models.DateField()
    nombre_proveedor = models.CharField(max_length=50)
    datos_contacto = models.CharField(max_length=500)
    detalles_oferta = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre

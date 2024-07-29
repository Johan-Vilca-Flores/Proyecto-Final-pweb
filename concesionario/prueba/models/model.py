from django.db import models
from .brands import Brands

class CarModel(models.Model):
    nombre = models.CharField(null=False, blank=False, max_length=255)
    marca = models.ForeignKey(Brands, on_delete=models.CASCADE)
    año = models.IntegerField(null=False)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=True, null=False)
    creado = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modificado = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.nombre


from django.db import models

class Dealers(models.Model):
    nombre = models.CharField(null=False, blank=False, max_length=255)
    direccion = models.CharField(null=True, blank=True, max_length=255)
    telefono = models.CharField(null=True, blank=True, max_length=255)
    correo_electronico = models.EmailField(unique=True, null=True, blank=True, max_length=255)
    estado = models.BooleanField(default=True, null=False)
    creado = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modificado = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.nombre

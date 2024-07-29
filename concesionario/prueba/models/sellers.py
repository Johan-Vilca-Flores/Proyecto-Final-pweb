from django.db import models

class Sellers(models.Model):
    nombres = models.CharField(null=False, blank=False, max_length=155)
    apellido_paterno = models.CharField(null=False, blank=False, max_length=155)
    apellido_materno = models.CharField(null=False, blank=False, max_length=155)
    correo_electronico = models.EmailField(unique=True, null=True, blank=True, max_length=255)
    telefono = models.CharField(null=True, blank=True, max_length=255)
    estado = models.BooleanField(default=True, null=False)
    creado = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modificado = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        ordering = ['nombres', 'apellido_paterno', 'apellido_materno']

    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellido_paterno = self.apellido_paterno.upper()
        self.apellido_materno = self.apellido_materno.upper()
        return super(Sellers, self).save(*args, **kwargs)

    def __str__(self):
        return " %s %s %s" % (self.nombres, self.apellido_paterno, self.apellido_materno)


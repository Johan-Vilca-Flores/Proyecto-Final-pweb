from django.db import models
from .model import CarModel
from .customer import Customer
from .dealers import Dealers

class Sales(models.Model):
    modelo = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE)
    concesionario = models.ForeignKey(Dealers, on_delete=models.CASCADE)
    fecha_venta = models.DateField(null=False)
    monto = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True, null=False)
    creado = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modificado = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return "Venta de %s a %s el %s" % (self.modelo, self.cliente, self.fecha_venta)



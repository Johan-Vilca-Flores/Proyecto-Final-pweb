from django.db import models
from .customer import Customer

class Pay(models.Model):
    monto = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    fecha = models.DateField(null=False)
    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True, null=False)
    creado = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modificado = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return "Pago de %s el %s" % (self.monto, self.fecha)




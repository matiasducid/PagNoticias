from django.db import models

# Create your models here.

class Cliente (models.Model):
    DNI_CUIT = models.CharField(max_length = 14)
    Nombres = models.CharField(max_length = 50)
    Apellidos = models.CharField(max_length = 50)
    Direccion = models.CharField(max_length = 50)
    Localidad = models.CharField(max_length = 100)
    Telefono = models.CharField(max_length = 30)
    TipoDeCliente = models.CharField(max_length = 7)
    DescuentoServicio = models.DecimalField(max_digits = 4, decimal_places = 2)
    #Se podria poner e-mail.
    DescuentoProducto = models.DecimalField(max_digits = 4, decimal_places = 2)
    CuentaCorriente = models.DecimalField(max_digits = 6, decimal_places = 2)#Son 6 digitos porque tiene un limite de adeudamiento de $3.000,00.

    def __str__ (self):
        return "{0}, {1}".format(self.Nombres,self.Apellidos)

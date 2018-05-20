from django.db import models

# Create your models here.



class Periodista(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    IdPeriodista = models.CharField(max_length=10)
    CantidadNoticiasEnviadas = models.CharField(max_length=5)

    def __str__(self):
        return "{0}, {1}.".format(self.Nombre,self.Apellido)


class Noticia(models.Model):
    Titulo = models.CharField(max_length=50)
    DescripcionContenido = models.CharField(max_length=100)
    Autor = models.ForeignKey(Periodista, null=False, blank=False, on_delete=models.CASCADE)
    Calidad = models.CharField( max_length=10)
    Puntaje = models.CharField(max_length=2)
    FechaCreacion = models.TimeField()
    FechaObservacion = models.CharField(max_length=10)
    GENERONOTICIA = (('P','Politica'),('F','Finanzas'),('C','Cultura'),('L','Laboral'),('D','Deportes'),('E','Educacion'),('O','Otro'))
    GeneroNoticia = models.CharField(max_length=1,choices=GENERONOTICIA,default='O')


    def detalleNoticia (self):
        cadena = "{0}, ({1})."
        return cadena.format(self.Titulo,self.DescripcionContenido)

    def __str__(self):
        return self.detalleNoticia()


class PedidoAlta(models.Model):
    Noticia = models.ForeignKey(Noticia, null=False, blank=False, on_delete=models.CASCADE)
    #Periodista = models.ForeignKey(Periodista, null=False, blank=False, on_delete=models.CASCADE)
    FechaPedido = models.DateTimeField(auto_now_add=True)
    NumeroPedido = models.CharField(max_length=5)

    def __str__(self):
        return "{0} - {1} - Calidad: {2}".format(self.NumeroPedido,self.Noticia,self.Noticia.Calidad)

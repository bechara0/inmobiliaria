from django.db import models
from django.utils import timezone


class Tipo_Serv(models.Model):
    tipo = models.CharField(
        max_length=100, help_text="Venta, Alquiler, Venta y Alquiler"
    )

    def __str__(self):
        return self.tipo


class Moneda(models.Model):
    moneda = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.moneda


class Localidad(models.Model):
    localidad = models.CharField(max_length=200)

    def __str__(self):
        return self.localidad


class Estado(models.Model):
    estado = models.CharField(max_length=50, help_text="Disponible?, Vendido?")

    def __str__(self):
        return self.estado


class Tipo(models.Model):
    tipo_propiedad = models.CharField(max_length=200, help_text="Casa, Depto, etc")

    def __str__(self):
        return self.tipo_propiedad


class Caracteristicas(models.Model):
    metros_cubiertos = models.IntegerField(blank=True, null=True)
    metros_terreno = models.IntegerField(blank=True, null=True)
    baños = models.IntegerField(blank=True, null=True)
    garage = models.IntegerField(blank=True, null=True)
    dormitorio = models.IntegerField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    moneda = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to="imagenes/", blank=True, null=True)


class Inmueble(models.Model):
    tipo_serv = models.ForeignKey(Tipo_Serv, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    lugar = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=200)
    amueblado = models.BooleanField(default=False)
    disponibilidad = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now, editable=False)
    caracteristicas = models.OneToOneField(
        Caracteristicas, on_delete=models.PROTECT, null=True, blank=True
    )

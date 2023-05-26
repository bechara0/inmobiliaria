from django.db import models
from django.utils import timezone


class Moneda(models.Model):
    moneda = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.moneda


class Localidad(models.Model):
    localidad = models.CharField(max_length=200)

    def __str__(self):
        return self.localidad


class Estado(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado


class Tipo(models.Model):
    tipo_propiedad = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo_propiedad


class Ventas(models.Model):
    lugar = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    metros_cubiertos = models.IntegerField(blank=True, null=True)
    metros_terreno = models.IntegerField(blank=True, null=True)
    baños = models.IntegerField(blank=True, null=True)
    cochera = models.IntegerField(blank=True, null=True)
    dormitorios = models.IntegerField(blank=True, null=True)
    amueblado = models.BooleanField(default=False)
    precio = models.IntegerField(blank=True, null=True)
    tipo_moneda = models.ForeignKey(
        Moneda, on_delete=models.PROTECT, null=True, blank=True
    )
    fecha_publicacion = models.DateTimeField(default=timezone.now, editable=False)
    disponibilidad = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="ventas_imagenes/", blank=True, null=True)


class Alquiler(models.Model):
    lugar = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    metros_cubiertos = models.IntegerField(blank=True, null=True)
    metros_terreno = models.IntegerField(blank=True, null=True)
    baños = models.IntegerField(blank=True, null=True)
    cochera = models.IntegerField(blank=True, null=True)
    dormitorios = models.IntegerField(blank=True, null=True)
    amueblado = models.BooleanField(default=False)
    precio = models.IntegerField(blank=True, null=True)
    tipo_moneda = models.ForeignKey(
        Moneda, on_delete=models.PROTECT, null=True, blank=True
    )
    fecha_publicacion = models.DateTimeField(default=timezone.now, editable=False)
    disponibilidad = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="alquiler_imagenes/")

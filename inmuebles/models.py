from django.db import models
from django.utils import timezone


class Tipo_Serv(models.model):
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


class Inmueble(models.Model):
    tipo_serv = models.ForeignKey(Tipo_Serv, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    lugar = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=200)
    amueblado = models.BooleanField(default=False)
    disponibilidad = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now, editable=False)


class Metros_cubiertos(models.Model):
    metros = models.OneToOneField(Inmueble, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        self.cantidad


class Metros_terreno(models.Model):
    metros = models.OneToOneField(Inmueble, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        self.cantidad


class Baños(models.Models):
    baños = models.OneToOneField(Inmueble, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        self.cantidad


class Garage(models.Models):
    garage = models.OneToOneField(Inmueble, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        self.cantidad


class Dormitorio(models.Models):
    dormitorio = models.OneToOneField(Inmueble, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        self.cantidad


class Precio(models.Models):
    precio = models.OneToOneField(Inmueble, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    moneda = models.ForeignKey(Moneda)

    def __str__(self):
        self.cantidad


class Imagen(models.Models):
    imagen = models.ImageField(upload_to="imagenes/", blank=True, null=True)

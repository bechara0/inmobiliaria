from django.contrib import admin
from .models import Alquiler, Ventas, Tipo, Estado, Localidad, Moneda


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ("localidad",)


class EstadoAdmin(admin.ModelAdmin):
    list_display = ("estado",)


class TipoAdmin(admin.ModelAdmin):
    list_display = ("tipo_propiedad",)


class VentasAdmin(admin.ModelAdmin):
    list_display = ("direccion", "lugar", "tipo")
    list_filter = ("lugar", "tipo", "fecha_publicacion")
    search_fields = ("lugar__localidad", "direccion", "tipo__nombre")


class AlquilerAdmin(admin.ModelAdmin):
    list_display = ("direccion", "lugar", "tipo", "disponibilidad")
    list_filter = ("lugar", "tipo", "fecha_publicacion", "disponibilidad")
    search_fields = ("lugar__localidad", "direccion", "tipo__nombre")


admin.site.register(Ventas, VentasAdmin)
admin.site.register(Alquiler, AlquilerAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Moneda)

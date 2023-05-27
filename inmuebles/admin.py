from django.contrib import admin
from .models import (
    Inmueble,
    Tipo,
    Estado,
    Localidad,
    Caracteristicas,
)


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ("localidad",)


class EstadoAdmin(admin.ModelAdmin):
    list_display = ("estado",)


class TipoAdmin(admin.ModelAdmin):
    list_display = ("tipo_propiedad",)


class InmuebleAdmin(admin.ModelAdmin):
    list_display = ("direccion", "lugar", "tipo", "tipo_serv")
    list_filter = ("lugar", "tipo", "fecha_publicacion", "tipo_serv")
    search_fields = ("lugar__localidad", "direccion", "tipo__nombre")


admin.site.register(Inmueble, InmuebleAdmin)

admin.site.register(Tipo, TipoAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Caracteristicas)

from django.contrib import admin

from . import models

admin.site.site_title = "Personajes"


class NivelMutanteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre", )


class PersonajeAdmin(admin.ModelAdmin):
    list_display = (
        "categoria_id",
        "nombre",
        "nombre_real",
        "poderes",
        "edad",
        "fecha_creacion",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("categoria_id", "nombre")
    list_filter = ("categoria_id",)

admin.site.register(models.NivelMutante, NivelMutanteAdmin)
admin.site.register(models.Personaje, PersonajeAdmin)
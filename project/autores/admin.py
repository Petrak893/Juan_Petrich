from django.contrib import admin
from . import models
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autores/', include('autores.urls')),
]

class AutorAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "es_dibujante",
        "es_escritor",
        "fecha_nacimiento",
        "biografia",
        "imagen"
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)
    list_filter = ("nombre",)

admin.site.register(models.Autor, AutorAdmin)
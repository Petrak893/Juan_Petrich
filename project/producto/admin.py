from django.contrib import admin

from . import models

admin.site.site_title = "Productos"

class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre", )
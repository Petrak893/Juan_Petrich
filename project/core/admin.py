from django.contrib import admin

from . import models

admin.site.site_title = "Personajes"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","profile_picture")

admin.site.register(models.Profile, ProfileAdmin)
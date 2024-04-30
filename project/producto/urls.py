from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.home, name="producto"),
    path("productocategoria/create/", views.productocategoria_create, name="productocategoria_create")
]
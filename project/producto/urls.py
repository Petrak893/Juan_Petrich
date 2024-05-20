from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.home, name="home"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(),
         name="productocategoria_list"),
    path("productocategoria/create/", views.ProductoCategoriaCreate.as_view(),
         name="productocategoria_create"),
    path("productocategoria/detail/", views.ProductoCategoriaDetail.as_view(),
         name="productocategoria_detail"),
    path("productocategoria/update/", views.ProductoCategoriaUpdate.as_view(),
         name="productocategoria_update"),
    path("productocategoria/delete/", views.ProductoCategoriaDelete.as_view(),
         name="productocategoria_delete"),
]

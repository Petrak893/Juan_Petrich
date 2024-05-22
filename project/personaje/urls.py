from django.urls import path

from . import views

app_name = "personaje"

urlpatterns = [
    path("", views.home, name="home"),
    path("nivelmutante/list/", views.NivelMutanteList.as_view(),
         name="nivelmutante_list"),
    path("nivelmutante/create/", views.NivelMutanteCreate.as_view(),
         name="nivelmutante_create"),
    path("nivelmutante/detail/<int:pk>", views.NivelMutanteDetail.as_view(),
         name="nivelmutante_detail"),
    path("nivelmutante/update/<int:pk>", views.NivelMutanteUpdate.as_view(),
         name="nivelmutante_update"),
    path("nivelmutante/delete/<int:pk>", views.NivelMutanteDelete.as_view(),
         name="nivelmutante_delete"),
]

urlpatterns += [
    path("personaje/list/", views.PersonajeList.as_view(),
         name="personaje_list"),
    path("personaje/create/", views.PersonajeCreate.as_view(),
         name="personaje_create"),
    path("personaje/detail/<int:pk>", views.PersonajeDetail.as_view(),
         name="personaje_detail"),
    path("personaje/update/<int:pk>", views.PersonajeUpdate.as_view(),
         name="personaje_update"),
    path("personaje/delete/<int:pk>", views.PersonajeDelete.as_view(),
         name="personaje_delete"),
]

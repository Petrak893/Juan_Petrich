from django.urls import path
from . import views

app_name = "autores"

urlpatterns = [
    path("", views.home, name="home"),
    path('autores/list', views.AutorListView.as_view(), name='autores_list'),
    path('autores/detail/<int:pk>', views.AutorDetailView.as_view(), name='autores_detail'),
    path('autores/create/', views.AutorCreateView.as_view(), name='autores_create'),
    path('autores/update/<int:pk>', views.AutorUpdateView.as_view(), name='autores_update'),
    path('autores/delete/<int:pk>', views.AutorDeleteView.as_view(), name='autores_delete'),
]
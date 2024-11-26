from django.urls import path
from plataforma_app import views

urlpatterns = [
    path("plataforma", views.inicio_vistaPlataforma, name="plataforma"),
    path("registrarPlataforma/", views.registrarPlataforma, name="registrarPlataforma"),
    path("borrarPlataforma/<codigo>", views.borrarPlataforma, name="borrarPlataforma"),
    path("seleccionarPlataforma/<codigo>", views.seleccionarPlataforma, name="seleccionarPlataforma"),
    path("editarPlataforma/", views.editarPlataforma, name="editarPlataforma")
]

from django.urls import path
from personal_app import views

urlpatterns = [
    path("personal", views.inicio_vistaPersonal, name="personal"),
    path("registrarPersonal/", views.registrarPersonal, name="registrarPersonal"),
    path("borrarPersonal/<codigo>", views.borrarPersonal, name="borrarPersonal"),
    path("seleccionarPersonal/<codigo>", views.seleccionarPersonal, name="seleccionarPersonal"),
    path("editarPersonal/", views.editarPersonal, name="editarPersonal")
]

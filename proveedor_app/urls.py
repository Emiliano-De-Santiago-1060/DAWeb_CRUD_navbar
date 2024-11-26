from django.urls import path
from proveedor_app import views

urlpatterns = [
    path("proveedor", views.inicio_vistaProveedor, name="proveedor"),
    path("registrarProveedor/", views.registrarProveedor, name="registrarProveedor"),
    path("borrarProveedor/<codigo>", views.borrarProveedor, name="borrarProveedor"),
    path("seleccionarProveedor/<codigo>", views.seleccionarProveedor, name="seleccionarProveedor"),
    path("editarProveedor/", views.editarProveedor, name="editarProveedor")
]

from django.urls import path
from . import views

urlpatterns = [
    path("alquiler/", views.alquiler, name="alquiler"),
    path("venta/", views.venta, name="venta"),
]

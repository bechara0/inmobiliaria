from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("quienes-somos", views.quienes_somos, name="quienes-somos"),
    path("servicios", views.servicios, name="servicios"),
]

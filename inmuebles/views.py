from django.shortcuts import render
from .models import Inmueble


def alquiler(request):
    alquileres = Inmueble.objects.filter(disponibilidad__in=[2, 3])
    context = {
        "alquileres": alquileres,
    }
    return render(request, "inmuebles/alquiler.html", context)


def venta(request):
    ventas = Inmueble.objects.filter(disponibilidad__in=[1, 3])
    context = {
        "ventas": ventas,
    }
    return render(request, "inmuebles/venta.html", context)


def todos(request):
    totalidad = Inmueble.objects.all()
    context = {
        "totalidad": totalidad,
    }
    return render(request, "inmuebles/todos.html", context)

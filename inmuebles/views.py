from django.shortcuts import render


def alquiler(request):
    return render(request, "inmuebles/alquiler.html")


def venta(request):
    return render(request, "inmuebles/venta.html")
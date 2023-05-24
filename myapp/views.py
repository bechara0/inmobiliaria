from django.shortcuts import render


def home(request):
    return render(request, "myapp/home.html")


def quienes_somos(request):
    return render(request, "myapp/quienes_somos.html")


def servicios(request):
    return render(request, "myapp/servicios.html")

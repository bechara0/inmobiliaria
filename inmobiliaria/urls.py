from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),
    path("contacto/", include("contacto.urls")),
    path("inmuebles/", include("inmuebles.urls")),
]

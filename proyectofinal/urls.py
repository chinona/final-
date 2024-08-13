from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ("", include("appfinal.urls")),
    path ("usuarios/", include("usuarios.urls")),
]



from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path ("login/", views.login_request, name="Login"),
    path("register/", views.register, name= "Register"),
    path("logout/", LogoutView.as_view(template_name="appfinal/inicio.html"), name= "Logout"),
    path("editar_perfil/", views.editar_perfil, name= "EditarPerfil"),
    path("cambiar_contrasenia/", views.CambiarContrasenia.as_view(), name= "CambiarContraseña")
]

from django.shortcuts import render
from appfinal.models import Artistas
from appfinal.models import Obras
from .models import Obras
from .models import Artistas
from django.views.generic import ListView
from appfinal.forms import CargarArtistaFormulario
# Create your views here.

def inicio(request):
    return render (request, "appfinal/inicio.html")

class ArtistasListView(ListView):
    model= Artistas
    context_object_name= "artistas"
    template_name= "appfinal/artistas.html"

class ObrasListView(ListView):
    model= Obras
    context_object_name= "obras"
    template_name= "appfinal/listar.html"

def acerca_de_mi(request):
    return render(request, "appfinal/acerca_de_mi.html")


def cargar_artista(request):
    if request.method == "POST":
        mi_formulario = CargarArtistaFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            artistas = Artistas(nombre=informacion["nombre"], provincia=informacion["provincia"], descripcion=informacion["descripcion"],mail_artista=informacion["mail"],pagina_web_redes_sociales=informacion["redes"], obras=informacion["obras"])
            artistas.save()

            return render(request, "appfinal/inicio.html")
    else:
        mi_formulario = CargarArtistaFormulario()

    return render(request, "appfinal/cargar_artista.html", {"mi_formulario": mi_formulario})


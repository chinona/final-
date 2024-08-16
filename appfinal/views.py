from django.shortcuts import render
from appfinal.models import Artistas
from appfinal.models import Obras
from .models import Obras
from .models import Artistas
from django.views.generic import ListView
from appfinal.forms import CargarArtistaFormulario
from appfinal.forms_obras import CargarObra
from django.contrib.auth.decorators import login_required
from appfinal.form_buscar import BuscaArtistaForm
from appfinal.form_buscar_obra import BuscaObraForm
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

@login_required
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

@login_required
def cargar_obra(request):
    if request.method == "POST":
        mi_formulario = CargarObra(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            obras = Obras(nombre=informacion["nombre"], provincia=informacion["provincia"], descripcion=informacion["descripcion"],mail_artista=informacion["mail"],pagina_web_redes_sociales=informacion["redes"], obras=informacion["obras"])
            obras.save()

            return render(request, "appfinal/inicio.html")
    else:
        mi_formulario = CargarObra()

    return render(request, "appfinal/cargar_obra.html", {"mi_formulario": mi_formulario})

def buscar_artista(request):
    if request.method == "POST":
        mi_formulario = BuscaArtistaForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            artistas = Artistas.objects.filter(nombre__icontains=informacion["artistas"])

            return render(request, "appfinal/mostrar_artistas.html", {"artistas": artistas})
    else:
        mi_formulario = BuscaArtistaForm()

    return render(request, "appfinal/buscar_artista.html", {"mi_formulario": mi_formulario})


def buscar_obra(request):
    if request.method == "POST":
        mi_formulario = BuscaObraForm(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            obras = Obras.objects.filter(nombre__icontains=informacion["obras"])

            return render(request, "appfinal/mostrar_obras.html", {"obras": obras})
    else:
        mi_formulario = BuscaObraForm()

    return render(request, "appfinal/buscar_obra.html", {"mi_formulario": mi_formulario})

def eliminarArtista(request, artista_nombre):
    artista= Artistas.objects.get(nombre=artista_nombre)
    artista.delete()

    artista= Artistas.objects.all()
    contexto={"artistas": artista}

    return render(request, "appfinal/eliminar_artista.html", contexto)
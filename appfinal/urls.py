from django.urls import path
from appfinal import views
from appfinal.views import inicio, acerca_de_mi

urlpatterns=[
    path("",inicio, name="inicio"),
    path("listar/", views.ObrasListView.as_view(), name= "listar"),
    path("artistas/", views.ArtistasListView.as_view(), name= "artistas"),
    path("acerca_de_mi", acerca_de_mi, name="acerca_de_mi"),
    path('cargar_artista', views.cargar_artista, name="cargar_artista"),
]


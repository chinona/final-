from django import forms
from django.db import models

class CargarArtistaFormulario(forms.Form):
    nombre= forms.CharField(max_length= 100)
    provincia= forms.CharField(max_length= 100)
    descripcion= forms.CharField(max_length= 600)
    mail_artista=forms.CharField(max_length= 200) 
    pagina_web_redes_sociales= forms.CharField(max_length= 300)
    imagenes= models.ImageField(upload_to='imagenes/', blank= True, null= True,)

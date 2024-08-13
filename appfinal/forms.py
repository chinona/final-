from django import forms

class CargarArtistaFormulario(forms.Form):
    nombre= forms.CharField(max_length= 100)
    provincia= forms.CharField(max_length= 100)
    descripcion= forms.CharField(max_length= 600)
    mail_artista=forms.CharField(max_length= 200) 
    pagina_web_redes_sociales= forms.CharField(max_length= 300)
    obras= forms.CharField(max_length=300)
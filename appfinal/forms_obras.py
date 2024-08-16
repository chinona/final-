from django import forms
from django.db import models

class CargarObra(forms.Form):
    nombre=models.CharField(max_length=100, null= True)
    autor= models.CharField(max_length=100, null= True)
    técnica= models.CharField(max_length= 50, null= True)
    año= models.CharField(max_length= 50, null= True)
    dimensiones= models.CharField(max_length= 50, null= True)
    tematica= models.CharField(max_length= 200, null= True)
    imagenes= models.ImageField(upload_to='imagenes/', blank= True, null= True)
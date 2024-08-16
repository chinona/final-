from django.db import models

# Create your models here.
class Artistas(models.Model):
    nombre= models.CharField(max_length= 100, null=True)
    provincia= models.CharField(max_length= 100, null=True)
    descripcion=models.CharField(max_length= 600)
    mail_artista=models.CharField(max_length= 200, null= True) 
    pagina_web_redes_sociales= models.CharField(max_length= 300)
    imagenes= models.ImageField(upload_to='imagenes/', blank= True, null= True)
    #obras= models.imagenes(null=True)

    def __str__(self):
        return f"nombre: {self.nombre} - provincia:{self.provincia} - descripcion:{self.descripcion} - mail del artista:{self.mail_artista} - redes: {self.pagina_web_redes_sociales} - imagenes:{self.imagenes}"
        
class Obras(models.Model):
    nombre=models.CharField(max_length=100, null= True)
    autor= models.CharField(max_length=100, null= True)
    técnica= models.CharField(max_length= 50, null= True)
    año= models.CharField(max_length= 50, null= True)
    dimensiones= models.CharField(max_length= 50, null= True)
    tematica= models.CharField(max_length= 200, null= True)
    imagenes= models.ImageField(upload_to='imagenes/', blank= True, null= True)

    def __str__(self):
        return f"nombre: {self.nombre} - autor: {self.autor} técnica:{self.técnica} - año:{self.año} - dimensiones:{self.dimensiones} - tematica: {self.tematica} - imagenes {self.imagenes}"

class Acerca_de_mi(models.Model):
    nombre= models.CharField(max_length= 50, null= True)



from django.db import models

# Create your models here.
class Artistas(models.Model):
    nombre= models.CharField(max_length= 100, null=True)
    provincia= models.CharField(max_length= 100, null=True)
    descripcion=models.CharField(max_length= 600)
    mail_artista=models.CharField(max_length= 200, null= True) 
    pagina_web_redes_sociales= models.CharField(max_length= 300)
    obras= models.CharField(max_length=300, null=True)
    #obras= models.imagenes(null=True)
    

class Obras(models.Model):
    nombre=models.CharField(max_length=100, null= True)
    técnica= models.CharField(max_length= 50, null= True)
    año= models.CharField(max_length= 50, null= True)
    dimensiones= models.CharField(max_length= 50, null= True)
    tematica= models.CharField(max_length= 200, null= True)

class Acerca_de_mi(models.Model):
    nombre= models.CharField(max_length= 50, null= True)



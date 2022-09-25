from distutils.command.upload import upload
from email.headerregistry import ContentDispositionHeader
from tabnanny import verbose
from tkinter import image_names
from django.db import models


# Create your models here.
class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.titulo
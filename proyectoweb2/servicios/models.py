from distutils.command.upload import upload
from email.headerregistry import ContentDispositionHeader
from tabnanny import verbose
from tkinter import image_names
from django.db import models

class Empresa(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Empresas'
        ordering=['nombre']
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.nombre

# Create your models here.
class Servicio(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=50,null=False)
    Contenido=models.CharField(max_length=100,null=False)
    imagen = models.ImageField(upload_to='servicios',null=False)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    empresa_id=models.OneToOneField(Empresa,on_delete=models.CASCADE)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        ordering=['titulo']
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.titulo
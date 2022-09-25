from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog',null=True,blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.titulo
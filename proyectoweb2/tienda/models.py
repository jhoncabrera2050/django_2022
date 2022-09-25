from re import T
from django.db import models

#creacion de modelos

class CategoriaProd(models.Model):
    nombre= models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoriaPro'
        verbose_name_plural='categoriasPro'
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda",null=True,blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.nombre


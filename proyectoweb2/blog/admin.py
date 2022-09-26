from django.contrib import admin

from .models import Categoria,Post
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=("id","nombre","created","updated")
    search_fields=("id","nombre")

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=("id","titulo","Contenido","autor","created","updated")
    search_fields=("id","titulo")
    list_filter=("autor",)
    
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post, PostAdmin)
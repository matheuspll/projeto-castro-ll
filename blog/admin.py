from django.contrib import admin
from .models import Post, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'criacao', 'atualizacao', 'categoria')
    prepopulated_fields = {'slug': ('titulo',)}


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    conteudo = RichTextUploadingField(null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        ordering = ('criacao',)

    def __str__(self):
        return f'{self.titulo} - {self.autor}'

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug, 'pk': self.id})


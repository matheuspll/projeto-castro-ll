from django.db import models
from django.template.defaultfilters import slugify


class Base(models.Model):
    """
    Classe abatrata, servindo apenas para compartilhar atributos.
    """
    criado = models.DateField(verbose_name='Data de Criação', auto_now_add=True)
    modificado = models.DateField(verbose_name='Data de Modificação', auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Categoria(Base):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome


class Produto(Base):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name='Descrição')
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(verbose_name='Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to='produtos')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
   
    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        """Sobrescrevendo o método save() e criando um slugify a partir do atributo nome"""
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)




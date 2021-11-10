from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Endereco (models.Model):
    rua = models.CharField(max_length=200, null=True,blank=False)
    numero = models.IntegerField(null=True, blank=False)
    complemento = models.CharField(max_length=200,null=True,blank=False)
    bairro = models.CharField(max_length=50,null=True,blank=False)
    cidade = models.CharField(max_length=100,null=True,blank=False)
    pais = models.CharField(max_length=50,null=True,blank=False)

    def __str__(self):
        return self.rua



class Pessoa (models.Model):
    nome = models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    telefone = models.CharField(max_length=1)
    Endereco = models.OneToOneField(Endereco,on_delete=CASCADE,default='P')
      
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.nome


class PessoaJuridica(Pessoa):
    comercial = "C"
    fixo = "F"
    pessoal = "P"
    TIPO_CHOICES = [
        (comercial, "Comercial"),
        (fixo, "Fixo"),
        (pessoal, "Pessoal")
    ]
    razao_social = models.CharField(max_length=200,verbose_name='Razão Social')
    nome_fantasia = models.CharField(max_length=200,verbose_name='Nome Fantasia')
    cnpj = models.CharField(max_length=15,unique=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default=pessoal)

    class meta:
        ordering= ['razao_social']


class PessoaFisica(Pessoa):
    sobre_nome: models.CharField(max_length=200, verbose_name='Sobrenome')
    cpf =models.CharField(max_length=14, unique=True)



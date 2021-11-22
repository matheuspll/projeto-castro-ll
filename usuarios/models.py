from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User

# Create your models here.


class Perfil(models.Model):
    nome_completo = models.CharField(max_length=100, null=True)
    cpf = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=16, null=True)
    usuario = OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.usuario)

    

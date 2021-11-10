from django.contrib import admin
from .models import Endereco,Pessoa,PessoaFisica,PessoaJuridica

# Register your models here.

admin.site.register(Endereco)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)

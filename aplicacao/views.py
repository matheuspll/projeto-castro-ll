from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PessoaFisica, PessoaJuridica, Produto


# ----------------- Cadastrar Produtos ----------------- #
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'marca', 'preco', 'estoque', 'imagem', 'categoria']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['tituloP']= "Cadastro de Produto"
        context['iconetitulo'] = '<i class="far fa-clipboard" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Produto"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar']='cadastrar'

        return context



# ----------------- Listar Produtos ----------------- #
class ProdutoListView(ListView):
    model = Produto


class ProdutoDetailView(DetailView):
    model = Produto


# ----------------- Atualizar Produtos ----------------- #
class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'marca', 'preco', 'estoque', 'imagem', 'categoria']
    template_name = 'aplicacao/form.html'
    success_url = reverse_lazy('home')





#-----------------   criar Cliente Pessoa Fisica ------------------------

class PessoaFisicaCreate(CreateView):
    model = PessoaFisica
    fields= ['nome','sobre','cpf','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Física"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar']='cadastrar'

        return context



class PessoaFisicaUpdate(UpdateView):
     model = PessoaFisica
     fields= ['nome','cpf','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
     template_name = 'aplicacao/formcliente.html'
     success_url = reverse_lazy('home')

     def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Atualizar Cliente Pessoa Física"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Atualizar'

        return context


     





#---------------------- Criar cliente Pessoa Juridica ---------------------------

class PessoaJuridicaCreate(CreateView):
    model = PessoaJuridica
    fields= ['nome','razao_social','cnpj','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fas fa-building" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Juridica"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar']='cadastrar'

        return context


class PessoaJuridicaUpdate(UpdateView):
    model = PessoaJuridica
    fields = ['nome','razao_social','cnpj','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fas fa-building" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Juridica"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar']='atualizar'

        return context 

    

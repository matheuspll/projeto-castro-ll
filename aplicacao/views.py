from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PessoaFisica, PessoaJuridica, Produto


# ----------------- Viwes Produtos ----------------- #

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'marca', 'preco', 'estoque', 'imagem', 'categoria']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('listagem-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
<<<<<<< HEAD

        context['tituloP']= "cadastro de Produto"
        context['icone_titulo'] = '<i class="far fa-clipboard" aria-hidden="true"></i>'
=======
        context['tituloP']= "Cadastro de Produto"
        context['iconetitulo'] = '<i class="" aria-hidden="true"></i>'
>>>>>>> d50a31ce57f52e3a48de04e8897db2e4fe9a40af
        context['titulo'] = "Cadastro de Produto"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Cadastrar'


        return context



class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'aplicacao/delete.html'
    success_url = reverse_lazy('listagem-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-exclamation" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Juridica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = 'excluir'

        return context

    
class ProdutoListView(ListView):
    model = Produto
    template_name = 'aplicacao/produto_list.html'



class ProdutoListagemListView(ListView):
    model = Produto
    template_name = 'aplicacao/list/list-produto.html'

    

class ProdutoDetailView(DetailView):
    model = Produto
    


class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'marca', 'preco', 'estoque', 'imagem', 'categoria']
    template_name = 'aplicacao/form.html'
    success_url = reverse_lazy('listagem-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Atualizar Produto"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Atualizar'

        return context

    



#-----------------   Views Pessoa Fisica ------------------------

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

<<<<<<< HEAD
=======

>>>>>>> d50a31ce57f52e3a48de04e8897db2e4fe9a40af
class PessoaFisicaDelete(DeleteView):
    model = PessoaFisica
    template_name = 'aplicacao/delete.html'
    success_url = reverse_lazy('indexadmin')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Pessoa Fisica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['icon2'] = '<i class = "fa fa-reply" aria-hidden = "true" > </i >'
        context['botao'] = 'Excluir'

        return context


class PessoaFisicaListagemListView(ListView):
    model = PessoaFisica
    template_name = 'aplicacao/list/list-cliente.html'
<<<<<<< HEAD
=======

>>>>>>> d50a31ce57f52e3a48de04e8897db2e4fe9a40af



#---------------------- Views Pessoa Juridica ---------------------------

class PessoaJuridicaCreate(CreateView):
    model = PessoaJuridica
    fields= ['nome','razao_social','cnpj','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-industry" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Juridica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'cadastrar'

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
        context['cadastrar'] = 'atualizar'

        return context 

    
class PessoaJuridicaDelete(DeleteView):
    model = PessoaJuridica
    template_name = 'aplicacao/delete.html'
    success_url = reverse_lazy('indexadmin')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Pessoa Juridica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['icon2'] = '<i class = "fa fa-reply" aria-hidden = "true" > </i >'
        context['botao'] = 'Excluir'

        return context

class PessoaJuridicaListagemListView(ListView):
    model = PessoaJuridica
    template_name = 'aplicacao/list/list-juridico.html'
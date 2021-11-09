from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Produto


# ----------------- Cadastrar Produtos ----------------- #
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'marca', 'preco', 'estoque', 'imagem', 'categoria']
    template_name = 'aplicacao/form.html'
    success_url = reverse_lazy('home')


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





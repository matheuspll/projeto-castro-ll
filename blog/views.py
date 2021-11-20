from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404
from braces.views import GroupRequiredMixin 



class PostCreateView(LoginRequiredMixin,CreateView):
    group_required = u"administradores"
    model = Post
    template_name = 'blog/post_cadastrar.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tituloP']= "Cadastro de Noticias Do Blog"
        context['iconetitulo'] = '<i class="" aria-hidden="true"></i>'
        context['titulo'] = "Postagem do Blog"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Postar'


        return context




class PostUpdateView(LoginRequiredMixin,GroupRequiredMixin,UpdateView):
    group_required = u"administradores"
    model = Post
    fields = '__all__'
    template_name = 'blog/post_cadastrar.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Atualizar Post "
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Atualizar'

        return context



class PostDeleteView(LoginRequiredMixin,GroupRequiredMixin,DeleteView):
    group_required = u"administradores"
    model = Post
    template_name = 'aplicacao/delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-exclamation" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Juridica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = 'excluir'

        return context





class PostListView(ListView):
    model = Post

    


class PostDetailView(DetailView):
    model = Post



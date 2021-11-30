from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.template.defaultfilters import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from aplicacao.views import CustomGroupRequiredMixin


class PostCreateView(LoginRequiredMixin, CreateView):
    group_required = u"administradores"
    model = Post
    template_name = 'blog/post_cadastrar.html'
    fields = ['titulo', 'conteudo', 'autor', 'categoria']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tituloP']= "Cadastro de Noticias Do Blog"
        context['iconetitulo'] = '<i class="" aria-hidden="true"></i>'
        context['titulo'] = "Postagem do Blog"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Postar'
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.slug = slugify(post.titulo)
        post.save()
        return super().form_valid(form)


class PostUpdateView(CustomGroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"administradores"
    model = Post
    fields = ['titulo', 'conteudo', 'autor', 'categoria']
    template_name = 'blog/post_cadastrar.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Atualizar Post "
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Atualizar'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.titulo)
        self.object.save()
        return super().form_valid(form)


class PostDeleteView(CustomGroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"administradores"
    model = Post
    template_name = 'aplicacao/delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-exclamation" aria-hidden="true"></i>'
        context['titulo'] = "Excluir Post"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = 'excluir'

        return context


class PostListView(ListView):
    model = Post

    
class PostDetailView(DetailView):
    model = Post


# -------------------- PORTAL --------------------- #
class PostListagemListView(CustomGroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/list-blog.html'

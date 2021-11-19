from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post



class PostCreateView(CreateView):
    model = Post
    field = ['titulo','slug','conteudo','autor','ativo','atualizacao','categoria']
    template_name = 'blog/formblog.html'
    success_url = reverse_lazy('portal')

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context['titulop']="Publicação de Post no Blog"
        context['icone_titulo']= '<i class="far fa-clipboard" aria-hidden="true"></i>'
        context['titulo']="Cadastro do Post"
        context['cadastrar']= 'postar'

        return context






class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post



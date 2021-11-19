from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
<<<<<<< HEAD
from django.views.generic import CreateView, UpdateView,DeleteView
=======
>>>>>>> d50a31ce57f52e3a48de04e8897db2e4fe9a40af
from django.urls import reverse_lazy
from .models import Post


<<<<<<< HEAD

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




=======
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_cadastrar.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
>>>>>>> d50a31ce57f52e3a48de04e8897db2e4fe9a40af


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post



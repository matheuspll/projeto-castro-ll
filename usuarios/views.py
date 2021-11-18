from django.views.generic.edit import CreateView,UpdateView

from django.contrib.auth.models import User,Group
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Perfil


class IndexAdmin (TemplateView):
    template_name = 'usuarios/indexadmin.html'



class UsuarioCreate(CreateView):
    template_name = 'aplicacao/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='publico')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url 


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['tituloP']= "Cadastros"
        context['iconetitulo'] = '<i class="fa fa-user" aria-hidden="true"></i>'
        context['titulo'] = "Cadastros de novos Usuários"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Cadastrar'

        return context



class PerfilUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Perfil
    fields = ['nome_completo','cpf','telefone']
    success_url = reverse_lazy('home')

    def get_object(self,queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)

        return self.object

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context['titulo'] = 'Meus dados pessoais'
        context['botão'] = 'Atualizar registro'

        return context




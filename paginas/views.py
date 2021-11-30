from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'


class PaginaSobre(TemplateView):
    template_name = 'paginas/sobre.html'


#---------------------- Contato FBV ---------------------------#
def contato(request):
    if request.method == 'POST': 
        data = {}
        data['nome'] = request.POST['nome']
        data['email'] = request.POST['email']
        data['assunto'] = request.POST['assunto']
        data['mensagem'] = request.POST['mensagem']

        mensagem = f"Nova Mensagem: {data['mensagem']}\nDe: {data['email']}"

        send_mail(data['assunto'], mensagem, '', ['mth.email.test@gmail.com'])
    return render(request, 'paginas/index.html', {})
    

#---------------------- Error Views ---------------------------#
def error_404(request, exception):
    return render(request, 'paginas/404.html')


def error_403(request, exception):
    return render(request, 'paginas/403.html')


def error_500(request):
    return render(request, 'paginas/500.html')


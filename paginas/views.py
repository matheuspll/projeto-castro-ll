from django.shortcuts import render
from django.views.generic import TemplateView


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'


class PaginaSobre(TemplateView):
    template_name = 'paginas/sobre.html'


# handler views - custom
def error_404(request, exception):
    return render(request, 'paginas/404.html')


def error_403(request, exception):
    return render(request, 'paginas/403.html')


def error_500(request):
    return render(request, 'paginas/500.html')


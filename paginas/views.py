from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name = 'index.html'

class PaginaSobre(TemplateView):
    template_name = 'sobre.html'
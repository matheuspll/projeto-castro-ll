from django.conf.urls import url
from django.urls import path
from .views import PaginaInicial, PaginaSobre
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', PaginaInicial.as_view(),name='home'),
    path('sobre/', PaginaSobre.as_view(),name='sobre'),
]
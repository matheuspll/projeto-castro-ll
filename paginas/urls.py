from django.urls import path
from .views import PaginaInicial, PaginaSobre
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', PaginaInicial.as_view(),name='home'),
]
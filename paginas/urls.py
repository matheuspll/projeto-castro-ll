from django.urls import path
from .views import PaginaInicial, PaginaSobre

urlpatterns = [
    path('index/', PaginaInicial.as_view(),name='index'),
    path('sobre/', PaginaSobre.as_view(),name='sobre'),
]
from django.urls import path

from .views import PessoaFisicaUpdate, PessoaJuridicaCreate,PessoaJuridicaUpdate    
from .views import ProdutoCreateView, ProdutoUpdateView, ProdutoListView, ProdutoDetailView

from .views import PessoaFisicaCreate

urlpatterns = [
    path('cadastrar/produto/', ProdutoCreateView.as_view(), name='cadastrar-produto'),
    path('produtos/', ProdutoListView.as_view(), name='produto-list'),
    path('produtos/<slug:slug>/<int:pk>/', ProdutoDetailView.as_view(), name='produto-detail'),
    path('editar/produto/<int:pk>/', ProdutoUpdateView.as_view(), name='produto-update'),

    path('cadastrar/pessoa-fisica/', PessoaFisicaCreate.as_view(), name='pessoa-fisica-cadastro'),
    path('cadastrar/pessoa-juridica/',PessoaJuridicaCreate.as_view(), name='pessoa-juridica-cadastro'),

    path('atualizar/pessoa-fisica/<int:pk>/', PessoaFisicaUpdate.as_view(), name='pessoa-fisica-atualizar'),
    path('atualizar/pessoa-juridica/<int:pk>/', PessoaJuridicaUpdate.as_view(), name='pessoa-juridica-atualizar'),

]

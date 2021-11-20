from django.urls import path

from .views import PessoaFisicaDelete, PessoaFisicaListagemListView, PessoaFisicaUpdate, PessoaJuridicaCreate, PessoaJuridicaDelete,PessoaJuridicaUpdate, ProdutoDeleteView, ProdutoListagemListView    
from .views import ProdutoCreateView, ProdutoUpdateView, ProdutoListView, ProdutoDetailView

from .views import PessoaFisicaCreate, ProdutoListagemListView, PessoaFisicaListagemListView, PessoaJuridicaListagemListView

urlpatterns = [
    path('cadastrar/produto/', ProdutoCreateView.as_view(), name='cadastrar-produto'),
    path('produtos/listar/', ProdutoListView.as_view(), name='produto-list'),
    path('produtos/<slug:slug>/<int:pk>/', ProdutoDetailView.as_view(), name='produto-detail'),
    path('editar/produto/<int:pk>/', ProdutoUpdateView.as_view(), name='produto-update'),
    path('deletar/produto/<int:pk>/', ProdutoDeleteView.as_view(), name='deletar-produto'),

    path('listagem/pessoa-juridica/', PessoaJuridicaListagemListView.as_view(),name='listagem-pessoa-juridica'),
    path('listagem/produtos/', ProdutoListagemListView.as_view(), name='listagem-produto'),
    path('listagem/pessoa-fisica/', PessoaFisicaListagemListView.as_view(), name='listagem-pessoa-fisica'),



    path('cadastrar/pessoa-fisica/', PessoaFisicaCreate.as_view(), name='pessoa-fisica-cadastro'),
    path('cadastrar/pessoa-juridica/',PessoaJuridicaCreate.as_view(), name='pessoa-juridica-cadastro'),

    path('atualizar/pessoa-fisica/<int:pk>/', PessoaFisicaUpdate.as_view(), name='pessoa-fisica-atualizar'),
    path('atualizar/pessoa-juridica/<int:pk>/', PessoaJuridicaUpdate.as_view(), name='pessoa-juridica-atualizar'),

    path('deletar/pessoa-fisica/<int:pk>/', PessoaFisicaDelete.as_view(), name='pessoa-fisica-deletar'),
    path('deletar/pessoa-juridica/<int:pk>/', PessoaJuridicaDelete.as_view(), name='pessoa-juridica-deletar'),


]

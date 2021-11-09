from django.urls import path
from .views import ProdutoListView, ProdutoDetailView
from .views import ProdutoCreateView, ProdutoUpdateView

urlpatterns = [
    path('cadastrar/produto/', ProdutoCreateView.as_view(), name='cadastrar-produto'),
    path('produtos/', ProdutoListView.as_view(), name='produto-list'),
    path('produtos/<slug:slug>/<int:pk>/', ProdutoDetailView.as_view(), name='produto-detail'),
    path('editar/produto/<int:pk>/', ProdutoUpdateView.as_view(), name='produto-update'),
]
from django.urls import path
from .views import PostDeleteView, PostListView, PostDetailView, PostCreateView, PostUpdateView

app_name = 'blog'
urlpatterns = [
    path('postagem/blog/', PostListView.as_view(), name='list'),
    path('informativos/<slug:slug>/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('postagem/cadastro/', PostCreateView.as_view(), name='postagem-cadastro'),
    path('postagem/atualizar/<int:pk>/', PostUpdateView.as_view(), name='postagem-atualizar'),
    path('postagem/deletar/<int:pk>/', PostDeleteView.as_view(),name='postagem-deletar'),
]
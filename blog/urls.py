from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

app_name = 'blog'
urlpatterns = [
    path('informativos/', PostListView.as_view(), name='list'),
    path('informativos/<slug:slug>/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('postagem/cadastro/', PostCreateView.as_view(), name='postagem-cadastro'),
<<<<<<< HEAD
    
=======
>>>>>>> d50a31ce57f52e3a48de04e8897db2e4fe9a40af
]
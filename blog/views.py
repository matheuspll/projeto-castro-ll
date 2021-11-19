from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Post


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_cadastrar.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post



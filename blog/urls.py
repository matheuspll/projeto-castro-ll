from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'blog'
urlpatterns = [
    path('informativos/', PostListView.as_view(), name='list'),
    path('informativos/<slug:slug>/<int:pk>/', PostDetailView.as_view(), name='detail'),
]
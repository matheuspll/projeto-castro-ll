from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate, IndexAdmin

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'usuarios/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('registrar/',UsuarioCreate.as_view(), name='registrar-usuarios'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
    path('portal/', IndexAdmin.as_view(), name='indexadmin'),    
]

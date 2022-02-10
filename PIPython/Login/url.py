from django.contrib import admin
from django.urls import path
from Login import views

urlpatterns = [
    # path('entrar/', views.Entrar, name="entrar"),
    path('cadastrar/', views.CadastroDeEmpresa, name="cadastro_empresa"),
    path('cadastrarEmpresa/', views.CadastrarEmpresa, name="cadastrar_empresa"),
    path('perfil/<int:id_empresa>', views.Perfil, name="perfil")
]

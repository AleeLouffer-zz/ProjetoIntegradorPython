from django.contrib import admin
from django.urls import path
from Login import views

urlpatterns = [
    # path('entrar/', views.Entrar, name="entrar"),
    path('cadastrar/', views.renderizar_tela_cadastro, name="cadastro_empresa"),
    path('cadastrarEmpresa/', views.cadastrar_empresa, name="cadastrar_empresa"),
    path('perfil/<int:id_empresa>', views.Perfil, name="perfil")
]

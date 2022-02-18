from django.contrib import admin
from django.urls import path
from Login import views

urlpatterns = [
    # path('entrar/', views.Entrar, name="entrar"),
    path('cadastrar/', views.renderizar_tela_cadastro, name="cadastro_empresa"),
    path('cadastrarEmpresa/', views.cadastrar_empresa, name="cadastrar_empresa"),
    path('perfil/<int:id_empresa>', views.Perfil, name="perfil")
    path("", views.tela_login, name="tela_login"),
    path("login", views.realizar_login, name="realizar_login"),

    # Arrumando CSS
    path("agendamentoTeste", views.tela_agendamento, name="tela_agendamento"),
    path("tela_agendamento_adicionar", views.tela_agendamento_adicionar, name="tela_agendamento_adicionar"),
    path("tela_agendamento_editar", views.tela_agendamento_editar, name="tela_agendamento_editar"),

    path("contas", views.tela_contas_a_receber, name="tela_contas_a_receber"),
    path("contas_adicionar", views.contas_adicionar, name="contas_adicionar"),
    
    path("prestador", views.prestador, name="prestador"),
]

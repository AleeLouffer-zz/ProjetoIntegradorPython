from django.urls import path
from .views import *

urlpatterns = [
    path('criar_funcionario', views_tela_inicial.cadastrar_funcionario, name="criar_funcionario"),
    path('criar_servico', views_tela_inicial.cadastrar_servico, name="criar_servico"),
    path('empresa/', views_tela_inicial.tela_inicial_prestador, name="tela_inicial_prestador"),
    path('verifica_botoes_funcionario', views_tela_inicial.verifica_botoes_funcionario, name="verifica_botoes_funcionario"),
    path('verifica_botoes_servico', views_tela_inicial.verifica_botoes_servico, name="verifica_botoes_servico"),
    path('botoes_cliente', views_tela_inicial.verifica_botoes_cliente, name="verifica_botoes_cliente"),
    path('criar_cliente', views_tela_inicial.cadastrar_cliente, name="criar_cliente"),
    path('agenda/', views_agendamentos.tela_agenda, name="tela_agenda"),
    path('agenda/adicionar_agendamento/', views_agendamentos.tela_adicionar_agendamento, name="tela_adicionar_agendamento"),
    path('agenda/add_agendamento', views_agendamentos.cadastrar_agendamento, name="adicionar_agendamento"),
    path('agenda/verifica_botoes_agendamento', views_agendamentos.verifica_botoes_agendamento, name="verifica_botoes_agendamento"),
    path('agenda/editar_agendamento', views_agendamentos.editar_agendamento, name="editar_agendamento"),
]

from django.contrib import admin
from django.urls import path
from Agendador import views
from .views import *

urlpatterns = [
    path('empresa/', views_tela_inicial.tela_inicial_prestador, name="tela_inicial_prestador"),
    path('editar_funcionario', views_tela_inicial.editar_funcionario, name="editar_funcionario"),
    path('editar_servico', views_tela_inicial.editar_servico, name="editar_servico"),
    path('agenda/', views_agendamentos.tela_agenda, name="tela_agenda"),
    path('agenda/adicionar_agendamento/', views_agendamentos.tela_adicionar_agendamento, name="tela_adicionar_agendamento"),
    path('agenda/add_agendamento', views_agendamentos.adicionar_agendamento, name="adicionar_agendamento"),
    path('agenda/verifica_botoes_agendamento', views_agendamentos.verifica_botoes_agendamento, name="verifica_botoes_agendamento"),
    path('agenda/editar_agendamento', views_agendamentos.editar_agendamento, name="editar_agendamento")
]

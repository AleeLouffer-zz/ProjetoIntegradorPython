from unicodedata import name
from django.contrib import admin
from django.urls import path
from Contas_a_Receber import views

app_name = "Contas_a_Receber"

urlpatterns = [
    path('contas_a_receber/', views.tela_contas_a_receber, name="tela_contas_a_receber"),
    path('adicionar_conta/', views.tela_adicionar_conta, name="adicionar_conta"),
    path('editar_conta/', views.tela_editar_conta, name="editar_conta"),
    path('adicionar_conta_agentamento/', views.tela_adicionar_conta_agendamento, name="adicionar_conta_agendamento"),
    path('verifica_botoes_conta_agendamento/', views.verifica_botoes_conta_agendamento, name="verifica_botoes_conta_agendamento"),
    path('verifica_botoes_adicionar_conta/', views.verifica_botoes_adicionar_conta, name="verifica_botoes_adicionar_conta"),
    path('verifica_botoes_editar_conta/', views.verifica_botoes_tela_editar, name="verifica_botoes_tela_editar"),
    path('verifica_botoes_tela_contas_a_receber/', views.verifica_botoes_tela_contas_a_receber, name="verifica_botoes_tela_contas_a_receber"),
    path('tela_pagamento/', views.tela_pagamento, name="tela_pagamento"),
    path('adicionar_forma_de_pagamento/', views.adicionar_forma_de_pagamento, name="adicionar_forma_de_pagamento"),
    path('atualizar_status_pagamento/', views.verifica_botoes_tela_pagamento, name="verifica_botoes_tela_pagamento"),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('filtrar/', views.filtrar, name="filtrar"),
]

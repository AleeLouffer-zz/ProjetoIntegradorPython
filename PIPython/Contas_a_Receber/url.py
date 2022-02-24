from django.contrib import admin
from django.urls import path
from Contas_a_Receber import views

urlpatterns = [
    path('contas_a_receber/', views.tela_contas_a_receber, name="tela_contas_a_receber"),
    path('adicionar_contas/', views.adicionar_conta, name="adicionar_conta"),
    path('editar_contas/', views.editar_conta, name="editar_conta")
]

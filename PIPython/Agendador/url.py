from django.contrib import admin
from django.urls import path
from Login import views

urlpatterns = [
    path('Empresa/<int:id_empresa>', views.tela_inicial_prestador, name="tela_inicial_prestador"),
    path('editar_funcionario', views.editar_funcionario, name="editar_funcionario"),
    path('editar_servico', views.editar_servico, name="editar_servico"),
    path('criar_funcionario', views.criar_funcionario, name="criar_funcionario"),
    path('criar_servico', views.criar_servico, name="criar_servico")
]

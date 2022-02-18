from django.contrib import admin
from django.urls import path
from Login import views

urlpatterns = [
    path('cadastrar/', views.renderizar_tela_cadastro, name="cadastro_empresa"),
    path('cadastrarEmpresa/', views.cadastrar_empresa, name="cadastrar_empresa"),
    path("", views.tela_login, name="tela_login"),
    path("login", views.realizar_login, name="realizar_login"),
    
    path("prestador", views.prestador, name="prestador"),
]
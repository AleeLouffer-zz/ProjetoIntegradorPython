from django.contrib import admin
from django.urls import path
from Login import views

app_name = 'Login'

urlpatterns = [
    path('cadastrar/', views.renderizar_tela_cadastro, name="cadastro_empresa"),
    path('cadastrar_empresa/', views.cadastrar_empresa, name="cadastrar_empresa"),
    path("", views.tela_login, name="tela_login"),
    path("login/", views.realizar_login, name="realizar_login"),
    path('editar_empresa/', views.editar_empresa, name="editarEmpresa"),
    path('deslogar',views.deslogar,name="sair"),
    path('sobre/', views.sobre, name='sobre')
]

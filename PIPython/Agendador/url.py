from django.contrib import admin
from django.urls import path
from Login import views


urlpatterns = [
    path('Empresa/<int: id_empresa>', views.tela_inicial_prestador, name="tela_inicial_prestador"),
]

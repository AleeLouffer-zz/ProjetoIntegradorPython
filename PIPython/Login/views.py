from django.shortcuts import render
from django.template import loader
from Agendador.views import *
from django.http import HttpResponse

# def Entrar(requisicao):
#     email = requisicao.POST['email']
#     senha = requisicao.POST['senha']

#     autenticate (email, senha)
#     autenticate.id_empresa

#     tela_inicial_prestador(id_empresa)
from django.shortcuts import render
from Agendador.views import *

def Tela_Inicial(requisicao):
    return render(requisicao, '../templates/telaPrestador.html')

def Entrar(requisicao):
    email = requisicao.POST['email']
    senha = requisicao.POST['senha']

    autenticate (email, senha)
    autenticate.id_empresa

    tela_inicial_prestador(id_empresa)
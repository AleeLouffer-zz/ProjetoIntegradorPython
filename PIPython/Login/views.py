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

def contas_a_receber(requisicao):
    return render(requisicao, '../templates/contasAReceber/contasAReceber.html')

def agenda_prestador(requisicao):
    return render(requisicao,'../templates/agendamento/agenda.html')
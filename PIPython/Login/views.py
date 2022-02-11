from django.shortcuts import render, redirect
from Agendador.views import *
from django.contrib.auth import authenticate, login
from Agendador.views import *

def tela_login(requisicao):
    return render(requisicao, '../templates/login/login.html')

def realizar_login(requisicao):
    email = requisicao.POST['email']
    senha = requisicao.POST['senha']
    
    user = authenticate(requisicao, username=email, password=senha)

    if user is not None:
        if user.is_active:
            login(requisicao, user)
            requisicao.session["id_empresa"] = user.id
            return redirect("/empresa/")
        
    else:
        return redirect(tela_login)


def tela_agendamento(requisicao):
    return render(requisicao, '../templates/agendamento/agenda.html')

def tela_agendamento_adicionar(requisicao):
    return render(requisicao, '../templates/agendamento/adicionar-agendamento.html')

def tela_agendamento_editar(requisicao):
    return render(requisicao, '../templates/agendamento/editar-agendamento.html')

def prestador(requisicao):
    return render(requisicao, '../templates/telaPrestador.html')

def tela_contas_a_receber(requisicao):
    return render(requisicao, '../templates/contasAReceber/contasAReceber.html')

def contas_adicionar(requisicao):
    return render(requisicao, '../templates/contasAReceber/adicionar.html')
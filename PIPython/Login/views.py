from django.shortcuts import render, redirect
from Agendador.views import *
from django.contrib.auth import authenticate, login

def tela_login(requisicao):
    return render(requisicao, '../templates/login/login.html')

def realizar_login(requisicao):
    email = requisicao.POST['email']
    senha = requisicao.POST['senha']

    user = authenticate(requisicao, username=email, password=senha)

    if user is not None:
        if user.is_active:
            login(requisicao, user)
            print(user.id)
            return redirect(tela_login)
        
    else:
        return redirect(tela_login)

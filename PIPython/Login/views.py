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

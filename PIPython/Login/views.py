from django.shortcuts import redirect, render
from Agendador.views import *
from django.contrib.auth import authenticate, login, logout
from Agendador.views import *
from Login.repo import *

def tela_login(requisicao):
    return render(requisicao, '../templates/login/login.html')

def renderizar_tela_cadastro(requisicao):
    return render(requisicao, 'telaCadastro.html')

def cadastrar_empresa(requisicao):
    razao_social = requisicao.POST['razao_social_cadastro']
    nome_fantasia = requisicao.POST['nome_cadastro']
    cnpj = requisicao.POST['cnpj_cadastro']
    email = requisicao.POST['email_cadastro']
    senha = requisicao.POST['senha_cadastro']

    criar_empresa_usuario(requisicao, email, senha, cnpj, nome_fantasia, razao_social)

    return redirect('Login:tela_login')
  
def realizar_login(requisicao):
    email = requisicao.POST['email']
    senha = requisicao.POST['senha']
    
    user = authenticate(requisicao, username=email, password=senha)

    empresa = obter_empresa_por_id(requisicao, user.id)

    if user is not None:
        if user.is_active:
            login(requisicao, user)
            requisicao.session["id_empresa"] = user.id
            requisicao.session["nome_empresa"] = empresa.nome_fantasia
            return redirect("/empresa/")
        
    else:
        return redirect('Login:tela_login')
    
def editar_empresa(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    nome_empresa = requisicao.POST['nome_empresa']
    email_empresa = requisicao.POST['email_empresa']
    senha_empresa = requisicao.POST['senha_empresa']

    atualizar_empresa(requisicao, id_empresa, nome_empresa, email_empresa, senha_empresa)

    return redirect('Agendador:tela_inicial_prestador')


def deslogar(requisicao):
    logout(requisicao)
    return redirect('Login:tela_login')

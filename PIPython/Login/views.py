from django.db import IntegrityError
from django.shortcuts import redirect, render
from Agendador.views import *
from django.contrib.auth import authenticate, login, logout
from Agendador.views import *
from Login.repo import *
from django.contrib import messages

def tela_login(requisicao):
    return render(requisicao, '../templates/login/login.html')

def renderizar_tela_cadastro(requisicao):
    return render(requisicao, 'telaCadastro.html')

def cadastrar_empresa(requisicao):
    nome = requisicao.POST['nome_cadastro']
    cnpj_cpf = requisicao.POST['cnpj_cpf_cadastro']
    email = requisicao.POST['email_cadastro']
    senha = requisicao.POST['senha_cadastro']

    try:
        criar_empresa_usuario(requisicao, email, senha, cnpj, nome_fantasia, razao_social)
        messages.success(requisicao, "Cadastro concluido com sucesso!")
        return redirect('Login:tela_login')
    except IntegrityError:
        messages.error(requisicao, "Empresa já cadastrada no sistema, por favor verifique o Email e CNPJ.")
        return redirect('Login:cadastro_empresa')
  
def realizar_login(requisicao):
    email = requisicao.POST['email']
    senha = requisicao.POST['senha']
    
    user = authenticate(requisicao, username=email, password=senha)

    if user is not None:
        if user.is_active:
            login(requisicao, user)
            empresa = obter_empresa_por_id(requisicao, user.id)
            requisicao.session["id_empresa"] = user.id
            requisicao.session["nome_empresa"] = empresa.nome
            return redirect("/empresa/")
        
    else:
        messages.error(requisicao, "Verifique seus dados e tente novamente!")
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
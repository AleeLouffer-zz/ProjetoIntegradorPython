from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from Agendador.views import *
from Login.models import Empresa

# Ir na branch do CRUD do prestador e refatorar
def Perfil(requisicao, id_empresa):
    print(id_empresa)

    return render(requisicao, 'telaPrestador.html')

# Autentica e manda para o perfil
# def Entrar(requisicao):
#     email = requisicao.POST['email']
#     senha = requisicao.POST['senha']

#     autenticate (email, senha)
#     autenticate.id_empresa

#     tela_inicial_prestador(id_empresa)

def CadastroDeEmpresa(requisicao):
    return render(requisicao, 'telaCadastro.html')

def CadastrarEmpresa(requisicao):
    nome = requisicao.POST['nome_cadastro']
    razao_social = requisicao.POST['razao_social_cadastro']
    CNPJ = requisicao.POST['cnpj_cadastro']
    email = requisicao.POST['email_cadastro']
    senha = requisicao.POST['senha_cadastro']

    Empresa.objects.create(nome_fantasia = nome, razao_social = razao_social, cnpj = CNPJ, email = email, senha = senha)

    empresa_cadastrada = Empresa.objects.get(cnpj=CNPJ)

    return redirect('perfil', empresa_cadastrada.id)
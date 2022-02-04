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

def editarEmpresa(requisicao):
    id_empresa = requisicao.POST['id_empresa']
    nome_empresa = requisicao.POST['nome_empresa']
    email_empresa = requisicao.POST['email_empresa']
    senha_empresa = requisicao.POST['senha_empresa']

    empresa = Empresa.objects.get(id = id_empresa)
    empresa.nome_fantasia = nome_empresa
    empresa.email = email_empresa
    empresa.senha = senha_empresa
    empresa.save()

    return redirect('tela_inicial_prestador', id_empresa = id_empresa)

        
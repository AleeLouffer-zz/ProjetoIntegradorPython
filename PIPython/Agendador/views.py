import json
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Empresa, Funcionario, Servico, Cliente, Agendamento
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

def busca_empresa(requisicao):
    razao_social = requisicao.POST['razao_social']
    nome_fantasia = requisicao.POST['nome_fantasia']
    cnpj = requisicao.POST['cnpj']
    email = requisicao.POST['email']
    senha = requisicao.POST['senha']

    empresa = Empresa(razao_social = razao_social, nome_fantasia = nome_fantasia, cnpj = cnpj, email = email, senha = senha)

    return empresa
    
@csrf_exempt
def criar_empresa(requisicao):
    empresa = busca_empresa(requisicao)

    try:
        empresa.save()
    except IntegrityError as e:
        if 'unique constraint' in e.message:
            print("Erro de duplicação no banco")

    return JsonResponse[{}]

def obtem_empresa(requisicao, id_da_empresa):
    empresa = Empresa.objects.get(id = id_da_empresa)

    response = {
        'empresa': empresa
    }

    return JsonResponse(response)


def update_empresa(requisicao, id_da_empresa):
    empresa = Empresa.objects.get(id = id_da_empresa)
    empresa.razao_social = requisicao.POST['razao_social']
    empresa.nome_fantasia = requisicao.POST['nome_fantasia']
    empresa.cnpj = requisicao.POST['cnpj']
    empresa.email = requisicao.POST['email']
    empresa.senha = requisicao.POST['senha']

    empresa.save()

    return JsonResponse({})

def criar_funcionario(requisicao):
    nome_funcionario =  requisicao.POST['nome_funcionario']
    
    funcionario = Funcionario(nome_funcionario = nome_funcionario)

    funcionario.save()

    return JsonResponse [{}]


def obtem_funcionario(requisicao, id_funcionario):
    funcionario = Funcionario.objects.get(id = id_funcionario)

    response = {
        'funcionario': funcionario
    }

    return JsonResponse(response)

def criar_sevico(requisicao):
    nome = requisicao.POST['nome']
    descricao = requisicao.POST['descricao']
    preco = requisicao.POST['preco']
    empresa = requisicao.POST['empresa']

    servico = Servico(nome = nome, descricao = descricao, preco = preco, empresa = empresa)

    servico.save()
    
    return JsonResponse[{}]
 
    
def obtem_servico(requisicao, id_servico):
    servico = Servico.objects.get(id = id_servico)

    response = {
        'servico': servico
    }
    
    return JsonResponse(response)

def criar_agendamento(requisicao):
    servico = requisicao.POST['servico']
    funcionario = requisicao.POST['funcionario']
    cliente = requisicao.POST['cliente']
    empresa = requisicao.POST['empresa']
    dataEHora = requisicao.POST['data_e_hora']

    agendamento = Agendamento(servico = servico, funcionario = funcionario, cliente = cliente, empresa = empresa, dataEHora = dataEHora)

    agendamento.save()

 
def obtem_agendamento(requisicao, id_do_agendamento):
    agendamento = Agendamento.objects.get(id = id_do_agendamento)

    response = {
        'agendamento': agendamento
    }

    return JsonResponse(response)


def criar_cliente(requisicao):
    nome = requisicao.POST['nome']
   
    cliente = Cliente(nome = nome)
    cliente 
    cliente.save()

    return JsonResponse({})


def obtem_cliente(requisicao, id_do_cliente):
    cliente = Cliente.objects.get(id = id_do_cliente)

    response = {
        'cliente': cliente
    }

    return JsonResponse(response)
    
    

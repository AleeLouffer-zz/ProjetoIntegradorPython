from django.shortcuts import render, redirect
from Login.models import Empresa
from Agendador.models import Agendamento, Funcionario, Cliente, Servico
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

def tela_agenda(requisicao):
    id_empresa = requisicao.session['id_empresa']
    funcionarios = obter_funcionarios(requisicao, id_empresa)
    servicos = obter_servicos(requisicao, id_empresa)
    
    if 'data' not in requisicao.POST:
        data = date.today()
        agendamentos = obter_agendamentos(requisicao, id_empresa, data)
        
    else:
        data = requisicao.POST['data']
        if data == "":
            data = date.today()
        agendamentos = list(obter_agendamentos(requisicao, id_empresa, data))

    if 'funcionario' in requisicao.POST:
        id_funcionario = requisicao.POST['funcionario']
        if id_funcionario != 'Todos Funcionários':
            agendamentos = list(filter(lambda x: x.funcionario.id == int(id_funcionario), agendamentos))

    if 'servico' in requisicao.POST:
        id_servico = requisicao.POST['servico']
        if id_servico != 'Todos Servicos':
            agendamentos = list(filter(lambda x: x.servico.id == int(id_servico), agendamentos))
        
    resposta = make_resposta(id_empresa, agendamentos, funcionarios, servicos)

    return render(requisicao, '../templates/agendamento/agenda.html', resposta)


def make_resposta(id_empresa, agendamentos, funcionarios, servicos):
    resposta = {
        'id_empresa': id_empresa,
        'agendamentos': agendamentos,
        'funcionarios': funcionarios,
        'servicos': servicos
    }
    return resposta


def obter_agendamentos(requisicao, id_empresa, data):
    return Agendamento.objects.filter(empresa=id_empresa).filter(data=data).order_by('hora')


def obter_funcionarios(requisicao, id_empresa):
    return list(Funcionario.objects.filter(empresa=id_empresa))


def obter_servicos(requisicao, id_empresa):
    return list(Servico.objects.filter(empresa=id_empresa))


def tela_adicionar_agendamento(requisicao):
    id_empresa = requisicao.session['id_empresa']

    clientes = Cliente.objects.filter(empresa=id_empresa)
    funcionarios = Funcionario.objects.filter(empresa=id_empresa)
    servicos = Servico.objects.filter(empresa=id_empresa)

    data = {
        'id_empresa': id_empresa,
        'clientes': list(clientes),
        'funcionarios': list(funcionarios),
        'servicos': list(servicos)
    }

    return render(requisicao, '../templates/agendamento/adicionar-agendamento.html', data)


def adicionar_agendamento(requisicao):
    id_empresa = requisicao.session['id_empresa']
    empresa = Empresa.objects.get(id=id_empresa)

    id_cliente = requisicao.POST['cliente']
    cliente = Cliente.objects.get(id=id_cliente)
    
    id_servico = requisicao.POST['servico']
    servico = Servico.objects.get(id=id_servico)
    
    id_funcionario = requisicao.POST['funcionario']
    funcionario = Funcionario.objects.get(id=id_funcionario)
    
    data_agendamento = requisicao.POST['data_agendamento']
    hora_agendamento = requisicao.POST['hora_agendamento'] ##ARRUMAR
    ##ADICIONAR VERIFICACAO
    
    agendamento = Agendamento(servico=servico, funcionario=funcionario, data=data_agendamento, hora=hora_agendamento, cliente=cliente, empresa=empresa)
    agendamento.save()

    return redirect('tela_agenda')

def verifica_botoes_agendamento(requisicao):
    if 'editar_agendamento' in requisicao.POST:
        data = obter_dados_tela_editar_agendamento(requisicao)
        return render(requisicao, '../templates/agendamento/editar-agendamento.html', data)
    elif 'excluir_agendamento' in requisicao.POST:
        excluir_agendamento(requisicao) 
        return redirect('tela_agenda')

def excluir_agendamento(requisicao):
    id_agendamento = requisicao.POST["id_agendamento"]
    agendamento = Agendamento.objects.get(id=id_agendamento)
    agendamento.delete()
        

def obter_dados_tela_editar_agendamento(requisicao):
    id_agendamento = requisicao.POST["id_agendamento"]
    id_empresa = requisicao.session["id_empresa"]

    agendamento = Agendamento.objects.get(id=id_agendamento)

    servicos = Servico.objects.filter(empresa=id_empresa)
    funcionarios = Funcionario.objects.filter(empresa=id_empresa)
    clientes = Cliente.objects.filter(empresa=id_empresa)

    dados = {
        'id_empresa': id_empresa,
        'agendamento': agendamento,
        'servicos': remover_da_lista(list(servicos), agendamento.servico),
        'funcionarios': remover_da_lista(list(funcionarios), agendamento.funcionario),
        'clientes': remover_da_lista(list(clientes), agendamento.cliente)
    }

    return dados

def remover_da_lista(lista, item_a_remover):
    for i in lista:
        if i == item_a_remover:
            lista.remove(item_a_remover)
    
    return lista

def editar_agendamento(requisicao):
    id_agendamento = requisicao.POST["id_agendamento"]

    data = requisicao.POST["data"]
    hora = requisicao.POST["hora_agendamento"]

    id_servico = requisicao.POST["id_servico"]
    servico = Servico.objects.get(id=id_servico)

    id_cliente = requisicao.POST["id_cliente"]
    cliente = Cliente.objects.get(id=id_cliente)

    id_funcionario = requisicao.POST["id_funcionario"]
    funcionario = Funcionario.objects.get(id=id_funcionario)

    agendamento = Agendamento.objects.get(id=id_agendamento)

    agendamento.servico = servico
    agendamento.cliente = cliente
    agendamento.funcionario = funcionario
    
    if data == "" or data == None:
        data = agendamento.data
    
    if hora == "" or hora == None:
        hora = agendamento.hora
    
    agendamento.data = data
    agendamento.hora = hora
    agendamento.save()
    

    return redirect('tela_agenda')
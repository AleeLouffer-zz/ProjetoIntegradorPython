from django.shortcuts import render, redirect
from Login.models import Empresa
from Agendador.models import Agendamento, Funcionario, Cliente, Servico
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

def tela_agenda(requisicao):
    if requisicao.method == 'POST':
        funcionarios = obter_funcionarios(requisicao, id_empresa)
        id_empresa = requisicao.POST['id_empresa']
        if 'data' not in requisicao.POST:
            data = date.today()
        else:
            data = requisicao.POST['data']

        agendamentos = obter_agendamentos(data)

    else:
        id_empresa = requisicao.GET['id_empresa']
        data = date.today()
        agendamentos = obter_agendamentos(requisicao, id_empresa, data)

        funcionarios = obter_funcionarios(requisicao, id_empresa)

    resposta = {
        'id_empresa': id_empresa,
        'data': data,
        'agendamentos': agendamentos,
        'funcionarios': funcionarios
    }

    return render(requisicao, '../templates/agendamento/agenda.html', resposta)
    
def obter_agendamentos(requisicao, id_empresa, data):
    return list(Agendamento.objects.filter(empresa=id_empresa).filter(dataEHora=data))

def obter_funcionarios(requisicao, id_empresa):
    return list(Funcionario.objects.filter(empresa=id_empresa))

def filtrar_agendamentos(requisicao, id_empresa, data=None, id_funcionario=None):
    if data == None or data == "":
        if id_funcionario == None or id_funcionario == "":
            agendamentos = Agendamento.objects.filter(empresa=id_empresa).filter(dataEHora=date.today()).filter(funcionario=id_funcionario)
        else:
            return HttpResponseRedirect(id_empresa)
    
    elif id_funcionario == None or id_funcionario == "":
        if data != None:
            agendamentos = Agendamento.objects.filter(empresa=id_empresa).filter(dataEHora=data)
        else:
            return HttpResponseRedirect(id_empresa)
    else:
        agendamentos = Agendamento.objects.filter(empresa=id_empresa).filter(dataEHora=data).filter(funcionario=id_funcionario)

    return agendamentos
    
def filtros_agenda(requisicao):
    id_empresa = requisicao.POST['id_empresa']
    data = requisicao.POST['data']
    if "None" in requisicao.POST['id_funcionario']:
        id_funcionario = None
    else:
        id_funcionario = requisicao.POST['id_funcionario']

    agendamentos = filtrar_agendamentos(requisicao, id_empresa, data, id_funcionario)

    funcionarios = obter_funcionarios(requisicao, id_empresa)

    agendamentos_e_funcionarios = {
        'id_empresa': id_empresa,
        'data': data,
        'agendamentos': list(agendamentos),
        'funcionarios': list(funcionarios)
    }

    return render(requisicao, '../templates/agendamento/agenda.html', agendamentos_e_funcionarios)

def tela_adicionar_agendamento(requisicao):
    id_empresa = requisicao.POST['id_empresa']

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
    id_empresa = requisicao.POST['id_empresa']
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
    agendamento = Agendamento(servico=servico, funcionario=funcionario, dataEHora=data_agendamento, cliente=cliente, empresa=empresa)
    agendamento.save()

    return redirect(id_empresa)

def verifica_botoes_agendamento(requisicao):
    if 'editar_agendamento' in requisicao.POST:
        data = obter_dados_tela_editar_agendamento(requisicao)
        return render(requisicao, '../templates/agendamento/editar-agendamento.html', data)
    elif 'excluir_agendamento' in requisicao.POST:
        excluir_agendamento() ##FAZER
        

def obter_dados_tela_editar_agendamento(requisicao):
    id_agendamento = requisicao.POST["id_agendamento"]
    id_empresa = requisicao.POST["id_empresa"]

    agendamento = Agendamento.objects.get(id=id_agendamento)

    servicos = Servico.objects.filter(empresa=id_empresa)
    funcionarios = Funcionario.objects.filter(empresa=id_empresa)
    clientes = Cliente.objects.filter(empresa=id_empresa)

    dados = {
        'id_emprea': id_empresa,
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
    data_e_hora = requisicao.POST["dataEHora"]
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
    
    if data_e_hora == "" or data_e_hora == None:
        data_e_hora = agendamento.dataEHora
    
    agendamento.dataEHora = data_e_hora
    agendamento.save()
    

    return HttpResponseRedirect(str(agendamento.empresa.id))
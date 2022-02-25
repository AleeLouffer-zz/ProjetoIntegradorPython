from os import remove
from re import I
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Contas_a_Receber.repo import *
from Login.repo import *
from Agendador.repo import *
from Agendador.views import *
from datetime import date

def tela_contas_a_receber(requisicao):
    id_empresa = requisicao.session["id_empresa"]

    data = {
        'contas_a_receber': list(obter_contas_da_empresa(requisicao, id_empresa)),
        'funcionarios': list(filtrar_funcionarios_ativos_por_id_empresa(requisicao, id_empresa)),
        'servicos': list(filtrar_servicos_ativos_por_id_empresa(requisicao, id_empresa)),
        'total_recebido': obter_totais_de_contas(requisicao, id_empresa, True),
        'total_a_receber': obter_totais_de_contas(requisicao, id_empresa, False)
    }

    return render(requisicao, '../templates/contas_a_receber/contas_a_receber.html', data)


def tela_editar_conta(requisicao):
    id_conta = requisicao.session["id_conta"]
    conta = obter_conta_por_id(requisicao, id_conta)
    
    id_empresa = requisicao.session['id_empresa']

    servicos = filtrar_servicos_ativos_por_id_empresa(requisicao, id_empresa)
    funcionarios = filtrar_funcionarios_ativos_por_id_empresa(requisicao, id_empresa)
    clientes = filtrar_clientes_ativos_por_id_empresa(requisicao, id_empresa)
    forma_de_pagamento = filtrar_formas_de_pagamentos_ativas_por_id_empresa(requisicao, id_empresa)

    data = {
        'conta': conta,
        'data_de_vencimento': str(conta.data_de_vencimento),
        'servicos': remover_da_lista(servicos, conta.servico),
        'funcionarios': remover_da_lista(funcionarios, conta.funcionario),
        'clientes': remover_da_lista(clientes, conta.cliente),
        'forma_de_pagamento': remover_da_lista(forma_de_pagamento, conta.forma_de_pagamento)
    }

    return render(requisicao, '../templates/contas_a_receber/editar.html', data)

def tela_adicionar_conta(requisicao):
    id_empresa = requisicao.session['id_empresa']

    data = {
        'data_de_emissao': date.today(),
        'servicos': list(filtrar_servicos_ativos_por_id_empresa(requisicao, id_empresa)),
        'funcionarios': list(filtrar_funcionarios_ativos_por_id_empresa(requisicao, id_empresa)),
        'clientes': list(filtrar_clientes_ativos_por_id_empresa(requisicao, id_empresa)),
        'formas_de_pagamento': list(filtrar_formas_de_pagamentos_ativas_por_id_empresa(requisicao, id_empresa))
    }

    return render(requisicao, '../templates/contas_a_receber/adicionar.html', data)

def verifica_botoes_adicionar_conta(requisicao):
    if 'cancelar' in requisicao.POST:
        return redirect('Contas_a_Receber:tela_contas_a_receber')
    
    elif 'adicionar' in requisicao.POST:
        adicionar_conta(requisicao)
        return redirect('Contas_a_Receber:tela_contas_a_receber')

def tela_adicionar_conta_agendamento(requisicao):
    id_agendamento = requisicao.session["id_agendamento"]
    id_empresa = requisicao.session["id_empresa"]

    agendamento = obter_agendamento_ativo_pelo_id(requisicao, id_agendamento)

    forma_de_pagamento = filtrar_formas_de_pagamentos_ativas_por_id_empresa(requisicao, id_empresa)

    dados = {
        'data_emissao': date.today(),
        'servico': agendamento.servico.nome,
        'funcionario': agendamento.funcionario.nome,
        'cliente': agendamento.cliente.nome,
        'valor': agendamento.servico.preco,
        'forma_de_pagamentos': list(forma_de_pagamento)
    }

    return render(requisicao, '../templates/contas_a_receber/adicionar_conta_agendamento.html', dados)

def verifica_botoes_conta_agendamento(requisicao):
    if 'cancelar' in requisicao.POST:
        del requisicao.session['id_agendamento']
        return redirect('Contas_a_Receber:tela_contas_a_receber')

    elif 'adicionar' in requisicao.POST:
        adicionar_conta(requisicao)
        return redirect('Contas_a_Receber:tela_contas_a_receber')

def adicionar_conta(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    if 'id_agendamento' in requisicao.session:
        id_agendamento = requisicao.session["id_agendamento"]

    data_de_vencimento = requisicao.POST['data_vencimento']
    data_de_emissao = date.today()
    id_forma_de_pagamento = requisicao.POST['forma_de_pagamento']

    if 'id_agendamento' in requisicao.session:
        criar_conta_a_receber_com_agendamento(requisicao, data_de_vencimento, data_de_emissao, id_forma_de_pagamento, id_empresa, id_agendamento)
        completar_agendamento(requisicao, id_agendamento)
        del requisicao.session['id_agendamento']

    else:
        valor = requisicao.POST['valor']
        id_funcionario = requisicao.POST['id_funcionario']
        id_servico = requisicao.POST['id_servico']
        id_cliente = requisicao.POST['id_cliente']
        criar_conta_a_receber(requisicao, valor, data_de_vencimento, data_de_emissao, id_forma_de_pagamento, id_funcionario, id_servico, id_cliente, id_empresa)

    return redirect('Contas_a_Receber:tela_contas_a_receber')

def editar_conta(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    id_conta = requisicao.session['id_conta']
    conta = obter_conta_por_id(requisicao, id_conta)

    data_de_vencimento = requisicao.POST['data_vencimento']
    id_forma_de_pagamento = requisicao.POST['forma_de_pagamento']
    forma_de_pagamento = obter_forma_de_pagamento_ativo_por_id(requisicao, id_forma_de_pagamento)

    if not conta.agendamento:
        id_funcionario = requisicao.POST['id_funcionario']
        funcionario = obter_funcionario_ativo_pelo_id(requisicao, id_funcionario)
        id_servico = requisicao.POST['id_servico']
        servico = obter_servico_ativo_pelo_id(requisicao, id_servico)
        id_cliente = requisicao.POST['id_cliente']
        cliente = obter_cliente_ativo_pelo_id(requisicao, id_cliente)
        atualizar_conta(requisicao, conta, data_de_vencimento, forma_de_pagamento, id_empresa, funcionario, servico, cliente)

    atualizar_conta(requisicao, conta, data_de_vencimento, forma_de_pagamento, id_empresa)

    del requisicao.session['id_conta']

def verifica_botoes_tela_contas_a_receber(requisicao):
    
    if 'editar' in requisicao.POST:
        requisicao.session['id_conta'] = requisicao.POST['id_conta']
        return redirect('Contas_a_Receber:editar_conta')
    elif 'tela_pagamento' in requisicao.POST:
        requisicao.session['id_conta'] = requisicao.POST['id_conta']
        return redirect('Contas_a_Receber:tela_pagamento')
    elif 'cancelar_pagamento' in requisicao.POST:
        atualiza_status_da_conta(requisicao)
        return redirect('Contas_a_Receber:tela_contas_a_receber')

def verifica_botoes_tela_editar(requisicao):
    if 'cancelar' in requisicao.POST:
        return redirect('Contas_a_Receber:tela_contas_a_receber')
    
    elif 'salvar' in requisicao.POST:
        editar_conta(requisicao)
        return redirect('Contas_a_Receber:tela_contas_a_receber')

def verifica_botoes_tela_pagamento(requisicao):
    if 'cancelar' in requisicao.POST:
        return redirect('Contas_a_Receber:tela_contas_a_receber')
    elif 'atualizar' in requisicao.POST:
        atualiza_status_da_conta(requisicao)
        return redirect('Contas_a_Receber:tela_contas_a_receber')

def atualiza_status_da_conta(requisicao):
    id_conta = requisicao.POST['conta']
    juros = requisicao.POST['juros']
    desconto = requisicao.POST['desconto']
    total = requisicao.POST['total']

    alterar_status_de_pagamento_da_conta(requisicao, id_conta, desconto, juros, total)

def tela_pagamento(requisicao):
    id_conta = requisicao.session['id_conta']
    conta = obter_conta_por_id(requisicao, id_conta)

    dados = {
        'valor': str(conta.valor)
    }

    return render(requisicao, '../templates/contas_a_receber/pagamento.html', dados)

def adicionar_forma_de_pagamento(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    forma_pagamento = requisicao.POST['forma_pagamento']
    criar_forma_de_pagamento(requisicao, id_empresa, forma_pagamento)

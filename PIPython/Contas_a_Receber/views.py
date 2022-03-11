from re import I
from django.shortcuts import render, redirect
from Contas_a_Receber.repo import *
from Login.repo import *
from Agendador.repo import *
from Agendador.views import *
from datetime import datetime
from django.http import JsonResponse


def atualizar_tela_atual(requisicao, tela_atual):
    requisicao.session["tela_atual"] = tela_atual

def tela_contas_a_receber(requisicao):
    atualizar_tela_atual(requisicao, 'Contas_a_Receber:tela_contas_a_receber')
    id_empresa = requisicao.session["id_empresa"]

    setar_filtros_sessao(requisicao)
    
    contas_a_receber = list(filtrar(requisicao))

    data = {
        'contas_a_receber': contas_a_receber,
        'funcionarios': list(filtrar_funcionarios_ativos_por_id_empresa(requisicao, id_empresa)),
        'servicos': list(filtrar_servicos_ativos_por_id_empresa(requisicao, id_empresa)),
        'clientes': list(filtrar_clientes_ativos_por_id_empresa(requisicao, id_empresa)),
        'total_recebido': obter_totais_de_contas_lista(requisicao, list(filter(lambda x: x.pago == True, contas_a_receber))),
        'total_a_receber': obter_totais_de_contas_lista(requisicao, list(filter(lambda x: x.pago == False, contas_a_receber)))
    }

    return render(requisicao, '../templates/contas_a_receber/contas_a_receber.html', data)

def obter_totais_de_contas_lista(requisicao, contas):
    total = 0
    
    for conta in contas:
        if conta.pago:
            total += conta.total
        else:
            total += conta.valor
    return total

def tela_editar_conta(requisicao):
    atualizar_tela_atual(requisicao, 'Contas_a_Receber:editar_conta')
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
    atualizar_tela_atual(requisicao, 'Contas_a_Receber:adicionar_conta')
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
    atualizar_tela_atual(requisicao, 'Contas_a_Receber:adicionar_conta_agendamento')
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
        return redirect('Agendador:tela_agenda')

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
        alterar_status_de_pagamento_da_conta(requisicao, requisicao.POST['id_conta'])
        return redirect('Contas_a_Receber:tela_contas_a_receber')

def verifica_botoes_tela_editar(requisicao):
    if 'cancelar' in requisicao.POST:
        return redirect('Contas_a_Receber:tela_contas_a_receber')
    
    elif 'salvar' in requisicao.POST:
        editar_conta(requisicao)
        return redirect('Contas_a_Receber:tela_contas_a_receber')

def tela_pagamento(requisicao):
    atualizar_tela_atual(requisicao, 'Contas_a_Receber:tela_pagamento')
    id_conta = requisicao.session['id_conta']
    conta = obter_conta_por_id(requisicao, id_conta)

    dados = {
        'valor': str(conta.valor)
    }

    return render(requisicao, '../templates/contas_a_receber/pagamento.html', dados)

def verifica_botoes_tela_pagamento(requisicao):
    if 'cancelar' in requisicao.POST:
        return redirect('Contas_a_Receber:tela_contas_a_receber')
    elif 'atualizar' in requisicao.POST:
        atualiza_status_da_conta(requisicao)
        return redirect('Contas_a_Receber:tela_contas_a_receber')

def atualiza_status_da_conta(requisicao):
    id_conta = requisicao.session['id_conta']
    data_de_pagamento = requisicao.POST['data_de_pagamento']
    juros = float(requisicao.POST['juros'])
    desconto = float(requisicao.POST['desconto'])
    total = float(requisicao.POST['total'])

    alterar_status_de_pagamento_da_conta(requisicao, id_conta, data_de_pagamento, total, desconto, juros)

def adicionar_forma_de_pagamento(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    forma_pagamento = requisicao.POST['forma_pagamento']
    criar_forma_de_pagamento(requisicao, id_empresa, forma_pagamento)
    return redirect(requisicao.session["tela_atual"])

def relatorio(requisicao):
    contas_a_receber = list(filtrar(requisicao))

    data = {
        'contas_a_receber': contas_a_receber,
        'total_recebido': obter_totais_de_contas_lista(requisicao, list(filter(lambda x: x.pago == True, contas_a_receber))),
        'total_a_receber': obter_totais_de_contas_lista(requisicao, list(filter(lambda x: x.pago == False, contas_a_receber))),
        'total_geral': obter_totais_de_contas_lista(requisicao, contas_a_receber)
    }

    return render(requisicao, '../templates/contas_a_receber/pdf.html', data)

def filtrar(requisicao):
    id_empresa = requisicao.session['id_empresa']
   
    contas = obter_contas_da_empresa_decrescente(requisicao, id_empresa)
    funcionariosFiltrados = filtrar_funcionario(requisicao, contas)
    servicosFiltrados = filtrar_servico(requisicao, funcionariosFiltrados)
    clientesFiltrados = filtrar_cliente(requisicao, servicosFiltrados)
    statusFiltrado = filtrar_por_status(requisicao, clientesFiltrados)
    dataFiltradaEmissao = filtrar_por_data_emissao(requisicao, statusFiltrado)
    dataFiltradaPagamento = filtrar_por_data_pagamento(requisicao, dataFiltradaEmissao)
    dataFiltradaVencimento = filtrar_por_data_vencimento(requisicao, dataFiltradaPagamento)

    return dataFiltradaVencimento

def setar_filtros_sessao(requisicao):
    verificar_filtro(requisicao, 'funcionario')
    verificar_filtro(requisicao, 'servico')
    verificar_filtro(requisicao, 'cliente')
    verificar_filtro(requisicao, 'status')
    verificar_filtro_data(requisicao, 'data_inicial--emissao')
    verificar_filtro_data(requisicao, 'data_final--emissao')
    verificar_filtro_data(requisicao, 'data_inicial--pagamento')
    verificar_filtro_data(requisicao, 'data_final--pagamento')
    verificar_filtro_data(requisicao, 'data_inicial--vencimento')
    verificar_filtro_data(requisicao, 'data_final--vencimento')

def verificar_filtro(requisicao, filtro):
    if filtro in requisicao.POST:
        requisicao.session[filtro] = requisicao.POST[filtro]
    else:
        requisicao.session[filtro] = 'todos'

def verificar_filtro_data(requisicao, filtro):
    if filtro in requisicao.POST:
        if requisicao.POST[filtro]:
            requisicao.session[filtro] = requisicao.POST[filtro]
        else: 
            requisicao.session[filtro] = 'sem data'
    else:
        requisicao.session[filtro] = 'sem data'

def filtrar_funcionario(requisicao, lista):
    if requisicao.session['funcionario'] != 'todos':
        funcionario = requisicao.session['funcionario']
        if funcionario != 'todos_funcionarios':
            return list(filter(lambda x: x.funcionario.id == int(funcionario), lista))
    
    return lista

def filtrar_servico(requisicao, lista):
    if requisicao.session['servico'] != 'todos':
        servico = requisicao.session['servico']
        if servico != 'todos_servicos':
            return list(filter(lambda x: x.servico.id == int(servico), lista))

    return lista

def filtrar_cliente(requisicao, lista):
    if requisicao.session['cliente'] != 'todos':
        cliente = requisicao.session['cliente']
        if cliente != 'todos_clientes':
            return list(filter(lambda x: x.cliente.id == int(cliente), lista))
            
    return lista

def filtrar_por_status(requisicao, lista):
    if requisicao.session['status'] != 'todos':
        status = requisicao.session['status']
        if status == '0':
            return lista
        if status == '1':
            return list(filter(lambda x: x.pago == False, lista))  
        if status == '2':
            return list(filter(lambda x: x.pago == True, lista))
    return lista

def obter_data_sessao(requisicao, data):
    if requisicao.session[data] != "sem data":
        return datetime.strptime(requisicao.session[data], '%Y-%m-%d').date()
    return None

def filtrar_por_data_emissao(requisicao, lista):
    data_inicial = obter_data_sessao(requisicao, 'data_inicial--emissao')
    data_final = obter_data_sessao(requisicao, 'data_final--emissao')
    
    if data_inicial and data_final:
       return list(filter(lambda x:x.data_de_emissao >= data_inicial and x.data_de_emissao <= data_final, lista))
    elif data_inicial:
        return list(filter(lambda x:x.data_de_emissao >= data_inicial, lista))
    elif data_final:
        return list(filter(lambda x:x.data_de_emissao <= data_final, lista))

    return lista

def filtrar_por_data_vencimento(requisicao, lista):
    data_inicial = obter_data_sessao(requisicao, 'data_inicial--vencimento')
    data_final = obter_data_sessao(requisicao, 'data_final--vencimento')

    if data_inicial and data_final:
        return list(filter(lambda x:x.data_de_vencimento != None and x.data_de_vencimento >= data_inicial and x.data_de_vencimento <= data_final, lista))
    elif data_inicial:
        return list(filter(lambda x:x.data_de_vencimento != None and x.data_de_vencimento >= data_inicial, lista))        
    elif data_final:
        return list(filter(lambda x:x.data_de_vencimento != None and x.data_de_vencimento <= data_final, lista))

    return lista

def filtrar_por_data_pagamento(requisicao, lista):
    data_inicial = obter_data_sessao(requisicao, 'data_inicial--pagamento')
    data_final = obter_data_sessao(requisicao, 'data_final--pagamento')
    
    if data_inicial and data_final:
        return list(filter(lambda x:x.data_de_pagamento != None and x.data_de_pagamento >= data_inicial and x.data_de_pagamento <= data_final, lista))
    elif data_inicial:
        return list(filter(lambda x:x.data_de_pagamento != None and x.data_de_pagamento >= data_inicial, lista))        
    elif data_final:
        return list(filter(lambda x:x.data_de_pagamento != None and x.data_de_pagamento <= data_final, lista))

    return lista
from django.shortcuts import render, redirect
from Contas_a_Receber.repo import *
from Login.repo import *
from Agendador.repo import *
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


def editar_conta(requisicao):
    id_conta = requisicao.POST["id_conta"]

    data = {
        'id_conta': id_conta
    }

    return render(requisicao, '../templates/contas_a_receber/editar.html', data)

def adicionar_conta(requisicao):
    return render(requisicao, '../templates/contas_a_receber/adicionar.html')

def adicionar_conta_agendamento(requisicao):
    id_agendamento = requisicao.session["id_agendamento"]
    id_empresa = requisicao.session["id_empresa"]

    agendamento = obter_agendamento_ativo_pelo_id(requisicao, id_agendamento)

    forma_de_pagamento = obter_forma_de_pagamento_ativo_por_id_empresa(requisicao, id_empresa)

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
        add_conta(requisicao)
        return redirect('Contas_a_Receber:tela_contas_a_receber')

def add_conta(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    id_agendamento = requisicao.session["id_agendamento"]

    valor = float(requisicao.POST['valor'])

    
    desconto = requisicao.POST['desconto']
    if desconto == '' or desconto == None:
        desconto = 0
    
    juros = requisicao.POST['juros']
    if juros == '' or juros == None:
        juros = 0

    total = (valor-desconto)+juros
    ## pago = adicionar verificacao no switch
    ## data_de_pagamento = verificar

    data_de_vencimento = requisicao.POST['data_vencimento']
    data_de_emissao = date.today()
    id_forma_de_pagamento = requisicao.POST['forma_de_pagamento']

    criar_conta_a_receber(requisicao, valor, desconto, juros, total, data_de_vencimento, data_de_emissao, id_forma_de_pagamento, id_agendamento, id_empresa)
    completar_agendamento(requisicao, id_agendamento)

    del requisicao.session['id_agendamento']

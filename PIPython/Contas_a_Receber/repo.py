from argparse import ArgumentError
from Contas_a_Receber.models import Forma_de_Pagamento, Contas_a_Receber
from Agendador.repo import *
from Login.repo import *

def filtrar_formas_de_pagamentos_ativas_por_id_empresa(requisicao, id_empresa):
    return list(Forma_de_Pagamento.objects.filter(empresa=id_empresa).filter(ativo=True))

def obter_forma_de_pagamento_ativo_por_id(requisicao, id_forma_de_pagamento):
    return Forma_de_Pagamento.objects.get(id=id_forma_de_pagamento)

def obter_totais_de_contas(requisicao, id_empresa, situacao_pagamento):
    contas =  Contas_a_Receber.objects.filter(empresa = id_empresa).filter(ativo = True).filter(pago = situacao_pagamento)
    total = 0
    for conta in contas:
        total += conta.valor
    return total

def obter_contas_da_empresa(requisicao, id_empresa):
    return Contas_a_Receber.objects.filter(empresa = id_empresa).filter(ativo=True)  

def obter_conta_por_id(requisicao, id_conta):
    return Contas_a_Receber.objects.get(id= id_conta)

def criar_conta_a_receber_com_agendamento(requisicao, data_de_vencimento, data_de_emissao, id_forma_de_pagamento, id_empresa, id_agendamento):
    agendamento = obter_agendamento_ativo_pelo_id(requisicao, id_agendamento)
    empresa = obter_empresa_por_id(requisicao, id_empresa)
    forma_de_pagamento = obter_forma_de_pagamento_ativo_por_id(requisicao, id_forma_de_pagamento)
    
    conta = Contas_a_Receber.objects.create(
        valor = agendamento.servico.preco, 
        data_de_vencimento = data_de_vencimento, 
        data_de_emissao = data_de_emissao, 
        forma_de_pagamento = forma_de_pagamento, 
        funcionario = agendamento.funcionario,
        servico = agendamento.servico,
        cliente = agendamento.cliente,
        agendamento = agendamento, 
        empresa = empresa)

    conta.save()

def criar_conta_a_receber(requisicao, valor, data_de_vencimento, data_de_emissao, id_forma_de_pagamento, id_funcionario, id_servico, id_cliente, id_empresa):
    funcionario = obter_funcionario_ativo_pelo_id(requisicao, id_funcionario)
    servico = obter_servico_ativo_pelo_id(requisicao, id_servico)
    cliente = obter_cliente_ativo_pelo_id(requisicao, id_cliente)
    empresa = obter_empresa_por_id(requisicao, id_empresa)
    forma_de_pagamento = obter_forma_de_pagamento_ativo_por_id(requisicao, id_forma_de_pagamento)

    conta = Contas_a_Receber.objects.create(
        valor = valor, 
        data_de_vencimento = data_de_vencimento, 
        data_de_emissao = data_de_emissao, 
        forma_de_pagamento = forma_de_pagamento, 
        funcionario = funcionario,
        servico = servico,
        cliente = cliente,
        empresa = empresa)

    conta.save()


def atualizar_conta(requisicao, conta, data_de_vencimento,forma_de_pagamento, id_empresa, funcionario=None, servico=None, cliente=None):
   empresa = obter_empresa_por_id(requisicao, id_empresa)

   conta.data_de_vencimento = data_de_vencimento
   conta.forma_de_pagamento = forma_de_pagamento
   
   if funcionario != None:
    conta.funcionario = funcionario
   if servico != None:
    conta.servico = servico
   if cliente != None:
    conta.cliente = cliente

   conta.empresa = empresa

   conta.save()

def alterar_status_de_pagamento_da_conta(requisicao, id_conta, desconto=None, juros=None, total=None):
    conta = obter_conta_por_id(requisicao, id_conta)

    if conta.pago:
        conta.desconto = 0
        conta.juros = 0
        conta.total = 0
        conta.pago = False
    else:
        conta.desconto = desconto
        conta.juros = juros
        total_da_conta = conta.valor + (juros - desconto)
        if total == total_da_conta:
            conta.total = total


def criar_forma_de_pagamento(requisicao, id_empresa, forma_pagamento):
    empresa = obter_empresa_por_id(requisicao, id_empresa)
    forma_de_pagamento = Forma_de_Pagamento.objects.create(nome = forma_pagamento, empresa = empresa)
    forma_de_pagamento.save()
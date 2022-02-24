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

def criar_conta_a_receber(requisicao, valor, desconto, juros, total, data_de_vencimento, data_de_emissao, id_forma_de_pagamento, id_empresa, id_agendamento=None):
    if id_agendamento != None:
        agendamento = obter_agendamento_ativo_pelo_id(requisicao, id_agendamento)
        empresa = obter_empresa_por_id(requisicao, id_empresa)
        forma_de_pagamento = obter_forma_de_pagamento_ativo_por_id(requisicao, id_forma_de_pagamento)

        conta = Contas_a_Receber.objects.create(valor = valor, desconto = desconto, juros = juros, total = total, 
        data_de_vencimento = data_de_vencimento, data_de_emissao = data_de_emissao, forma_de_pagamento = forma_de_pagamento, 
        agendamento = agendamento, empresa = empresa)
        conta.save()
    
    else:
        empresa = obter_empresa_por_id(requisicao, id_empresa)
        forma_de_pagamento = obter_forma_de_pagamento_ativo_por_id(requisicao, id_forma_de_pagamento)

        conta = Contas_a_Receber.objects.create(valor = valor, desconto = desconto, juros = juros, total = total, 
        data_de_vencimento = data_de_vencimento, data_de_emissao = data_de_emissao, forma_de_pagamento = forma_de_pagamento, 
        empresa = empresa)
        conta.save()
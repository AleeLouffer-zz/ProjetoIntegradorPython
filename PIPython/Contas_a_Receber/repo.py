from Contas_a_Receber.models import Forma_de_Pagamento, Contas_a_Receber

def obter_forma_de_pagamento_ativo_por_id_empresa(requisicao, id_empresa):
    return list(Forma_de_Pagamento.objects.filter(empresa=id_empresa).filter(ativo=True))

def obter_totais_de_contas(requisicao, id_empresa, situacao_pagamento):
    contas =  Contas_a_Receber.objects.filter(empresa = id_empresa).filter(ativo = True).filter(pago = situacao_pagamento)
    total = 0
    for conta in contas:
        total += conta.valor
    return total

def obter_contas_da_empresa(requisicao, id_empresa):
    return Contas_a_Receber.objects.filter(empresa = id_empresa).filter(ativo=True)  
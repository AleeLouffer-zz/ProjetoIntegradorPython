from django.shortcuts import render
from Contas_a_Receber.repo import *
from Login.repo import *
from Agendador.repo import *

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
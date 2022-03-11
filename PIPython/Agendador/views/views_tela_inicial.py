from django.shortcuts import render, redirect
from Agendador.repo import *
from Login.repo import *


def tela_inicial_prestador(requisicao):
    id_empresa = requisicao.session['id_empresa']

    empresa = obter_empresa_por_id(requisicao, id_empresa)

    dados = {
        'empresa': empresa,
        'funcionarios': list(filtrar_funcionarios_ativos_por_id_empresa(requisicao, id_empresa)),
        'servicos': list(filtrar_servicos_ativos_por_id_empresa(requisicao, id_empresa)),
        'clientes': list(filtrar_clientes_ativos_por_id_empresa(requisicao, id_empresa))
    }

    return render(requisicao, 'telaPrestador.html', dados)


def editar_funcionario(requisicao):
    id_funcionario = requisicao.POST['id_funcionario']
    nome_novo = requisicao.POST['nome_funcionario']
    
    atualizar_funcionario(requisicao, id_funcionario, nome_novo)
    

def editar_servico(requisicao):
    id_servico = requisicao.POST['servico_id']
    nome_servico = requisicao.POST['servico_nome']
    descricao_servico = requisicao.POST['servico_descricao']
    valor_servico = requisicao.POST['servico_valor']

    atualizar_servico(requisicao, id_servico, nome_servico, descricao_servico, valor_servico)


def cadastrar_funcionario(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    nome_funcionario = requisicao.POST['nome_funcionario']

    criar_funcionario(requisicao, id_empresa, nome_funcionario)

    return redirect('Agendador:tela_inicial_prestador')


def verifica_botoes_editar_empresa(requisicao):
    if 'editar' in requisicao.POST:
        editar_empresa(requisicao)
        return redirect('Agendador:tela_inicial_prestador')
    elif 'cancelar' in requisicao.POST:
        return redirect('Agendador:tela_inicial_prestador')


def editar_empresa(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    nome_empresa = requisicao.POST['nome_empresa']
    email_empresa = requisicao.POST['email_empresa']
    senha_empresa = requisicao.POST['senha_empresa']

    requisicao.session['nome_empresa'] = nome_empresa

    atualizar_empresa(requisicao, id_empresa, nome_empresa, email_empresa, senha_empresa)


def cadastrar_cliente(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    nome_cliente = requisicao.POST["nome_cliente"]

    criar_cliente(requisicao, id_empresa, nome_cliente)

    return redirect("Agendador:tela_inicial_prestador")


def cadastrar_servico(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    nome_servico = requisicao.POST['servico_nome']
    descricao_servico = requisicao.POST['servico_descricao']
    valor_servico = requisicao.POST['servico_valor']
    
    criar_servico(requisicao, id_empresa, nome_servico, descricao_servico, valor_servico)

    return redirect('Agendador:tela_inicial_prestador')


def excluir_servico(requisicao):
    id_servico = requisicao.POST["servico_id"]
    
    deletar_servico(requisicao, id_servico)


def excluir_funcionario(requisicao):
    id_funcionario = requisicao.POST["id_funcionario"]
    
    deletar_funcionario(requisicao, id_funcionario)


def verifica_botoes_funcionario(requisicao):
    if 'editar_funcionario' in requisicao.POST:
        editar_funcionario(requisicao)

        return redirect('Agendador:tela_inicial_prestador')
    elif 'excluir_funcionario' in requisicao.POST:
        excluir_funcionario(requisicao)

        return redirect('Agendador:tela_inicial_prestador')


def verifica_botoes_servico(requisicao):
    if 'editar_servico' in requisicao.POST:
        editar_servico(requisicao)

        return redirect('Agendador:tela_inicial_prestador')
    elif 'excluir_servico' in requisicao.POST:
        excluir_servico(requisicao)

    return redirect("Agendador:tela_inicial_prestador")


def verifica_botoes_cliente(requisicao):
    if 'editar_cliente' in requisicao.POST:
        editar_cliente(requisicao)
        return redirect("Agendador:tela_inicial_prestador")
    elif 'excluir_cliente' in requisicao.POST:
        excluir_cliente(requisicao) 
        return redirect('Agendador:tela_inicial_prestador')


def editar_cliente(requisicao):
    id_cliente = requisicao.POST['id_cliente']
    nome_novo = requisicao.POST['nome_cliente']

    atualizar_cliente(requisicao, id_cliente, nome_novo)

    return redirect("Agendador:tela_inicial_prestador")


def excluir_cliente(requisicao):
    id_cliente = requisicao.POST['id_cliente']

    deletar_cliente(requisicao, id_cliente)

    return redirect("Agendador:tela_inicial_prestador")
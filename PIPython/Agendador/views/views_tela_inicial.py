from django.shortcuts import render, redirect
from Login.models import Empresa
from Agendador.models import Agendamento, Funcionario, Cliente, Servico
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

def tela_inicial_prestador(requisicao):
    id_empresa = requisicao.session['id_empresa']

    empresa = Empresa.objects.get(id=id_empresa)

    dados = {
        'empresa': empresa,
        'funcionarios': list(obter_funcionarios(id_empresa)),
        'servicos': list(obter_servicos(id_empresa)),
        'clientes': list(obter_clientes(id_empresa))
    }

    return render(requisicao, 'telaPrestador.html', dados)

def obter_funcionarios(id_empresa):
    return Funcionario.objects.filter(empresa_id = id_empresa).filter(ativo=True)

def obter_servicos(id_empresa):
    return Servico.objects.filter(empresa_id = id_empresa).filter(ativo=True)

def obter_clientes(id_empresa):
    return Cliente.objects.filter(empresa_id = id_empresa).filter(ativo=True)

def editar_funcionario(requisicao):
    id_funcionario = requisicao.POST['id_funcionario']
    nome_novo = requisicao.POST['nome_funcionario']
    
    funcionario = Funcionario.objects.get(id=id_funcionario)
    
    funcionario.nome = nome_novo
    funcionario.save()

    return redirect('tela_inicial_prestador')
    
def editar_servico(requisicao):
    id_servico = requisicao.POST['servico_id']
    nome_servico = requisicao.POST['servico_nome']
    descricao_servico = requisicao.POST['servico_descricao']
    valor_servico = requisicao.POST['servico_valor']

    servico = Servico.objects.get(id=id_servico)
    servico.nome = nome_servico
    servico.descricao = descricao_servico
    servico.preco = float(valor_servico)
    servico.save()

    return redirect('tela_inicial_prestador')

def criar_cliente(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    nome_cliente = requisicao.POST["nome_cliente"]

    empresa = Empresa.objects.get(id=id_empresa)

    cliente = Cliente.objects.create(nome=nome_cliente, empresa=empresa)
    cliente.save()

    return redirect("tela_inicial_prestador")

def verifica_botoes_cliente(requisicao):
    if 'editar_cliente' in requisicao.POST:
        editar_cliente(requisicao)
        return redirect("tela_inicial_prestador")
    elif 'excluir_cliente' in requisicao.POST:
        excluir_cliente(requisicao) 
        return redirect('tela_inicial_prestador')

def editar_cliente(requisicao):
    id_cliente = requisicao.POST['id_cliente']
    nome_novo = requisicao.POST['nome_cliente']

    cliente = Cliente.objects.get(id=id_cliente)

    cliente.nome = nome_novo
    cliente.save()

    return redirect("tela_inicial_prestador")

def excluir_cliente(requisicao):
    id_cliente = requisicao.POST['id_cliente']

    cliente = Cliente.objects.get(id=id_cliente)

    cliente.ativo = False
    cliente.save()

    return redirect("tela_inicial_prestador")
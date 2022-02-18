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

def editarEmpresa(requisicao):
    id_empresa = requisicao.POST['id_empresa']
    nome_empresa = requisicao.POST['nome_empresa']
    email_empresa = requisicao.POST['email_empresa']
    senha_empresa = requisicao.POST['senha_empresa']

    empresa = Empresa.objects.get(id = id_empresa)
    empresa.nome_fantasia = nome_empresa
    empresa.email = email_empresa
    empresa.senha = senha_empresa
    empresa.save()

    return redirect('tela_inicial_prestador')

def editar_funcionario(requisicao):
    id_funcionario = requisicao.POST['id_funcionario']
    nome_novo = requisicao.POST['nome_funcionario']
    
    funcionario = Funcionario.objects.get(id=id_funcionario)
    
    funcionario.nome = nome_novo
    funcionario.save()
    
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

def criar_funcionario(requisicao):
    id_empresa = requisicao.POST['id_empresa']
    nome_funcionario = requisicao.POST['nome_funcionario']

    empresa_a_adicionar = Empresa.objects.get(id=id_empresa)

    Funcionario.objects.create(nome = nome_funcionario, empresa = empresa_a_adicionar)

    return redirect('tela_inicial_prestador')

def criar_cliente(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    nome_cliente = requisicao.POST["nome_cliente"]

    empresa = Empresa.objects.get(id=id_empresa)

    cliente = Cliente.objects.create(nome=nome_cliente, empresa=empresa)
    cliente.save()

    return redirect("tela_inicial_prestador")

def criar_servico(requisicao):
    id_empresa = requisicao.POST['id_empresa']
    nome_servico = requisicao.POST['nome_servico']
    valor_servico = requisicao.POST['valor_servico']
    descricao_servico = requisicao.POST['descricao_servico']

    empresa_a_adicionar = Empresa.objects.get(id=id_empresa)

    Servico.objects.create(nome = nome_servico, descricao = descricao_servico, preco = valor_servico, empresa = empresa_a_adicionar)

    return redirect('tela_inicial_prestador')

def excluir_servico(requisicao):
    id_servico = requisicao.POST["servico_id"]
    servico = Servico.objects.get(id=id_servico)
    servico.ativo = False
    servico.save()

def excluir_funcionario(requisicao):
    id_funcionario = requisicao.POST["id_funcionario"]
    funcionario = Funcionario.objects.get(id=id_funcionario)
    funcionario.ativo = False
    funcionario.save()

def verifica_botoes_funcionario(requisicao):
    if 'editar_funcionario' in requisicao.POST:
        editar_funcionario(requisicao)

        return redirect('tela_inicial_prestador')
    elif 'excluir_funcionario' in requisicao.POST:
        excluir_funcionario(requisicao)

        return redirect('tela_inicial_prestador')

def verifica_botoes_servico(requisicao):
    if 'editar_servico' in requisicao.POST:
        editar_servico(requisicao)

        return redirect('tela_inicial_prestador')
    elif 'excluir_servico' in requisicao.POST:
        excluir_servico(requisicao)

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
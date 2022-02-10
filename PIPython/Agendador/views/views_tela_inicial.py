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
        'servicos': list(obter_servicos(id_empresa))
    }

    return render(requisicao, 'telaPrestador.html', dados)

def obter_funcionarios(id_empresa):
    return Funcionario.objects.filter(empresa_id = id_empresa)

def obter_servicos(id_empresa):
    return Servico.objects.filter(empresa_id = id_empresa)

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



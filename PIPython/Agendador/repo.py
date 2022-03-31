from Agendador.models import Agendamento, Funcionario, Cliente, Servico
from Login.repo import *

def filtrar_agendamentos_ativos_por_data_e_id_empresa(requisicao, id_empresa, data):
    return Agendamento.objects.filter(empresa=id_empresa).filter(data=data).filter(ativo=True).order_by('hora')

def filtrar_agendamentos_ativos_por_periodo_data_e_id_empresa(requisicao, id_empresa, data_inicial, data_final):   
    return Agendamento.objects.filter(empresa=id_empresa, data__gte=data_inicial, data__lte=data_final, ativo=True).order_by('hora')

def filtrar_funcionarios_ativos_por_id_empresa(requisicao, id_empresa):
    return list(Funcionario.objects.filter(empresa=id_empresa).filter(ativo=True))

def filtrar_servicos_ativos_por_id_empresa(requisicao, id_empresa):
    return list(Servico.objects.filter(empresa=id_empresa).filter(ativo=True))

def filtrar_clientes_ativos_por_id_empresa(requisicao, id_empresa):
    return list(Cliente.objects.filter(empresa=id_empresa).filter(ativo=True))

def obter_agendamento_ativo_pelo_id(requisicao, id_agendamento):
    return Agendamento.objects.get(id=id_agendamento)

def obter_servico_ativo_pelo_id(requisicao, id_servico):
    return Servico.objects.get(id=id_servico)

def obter_cliente_ativo_pelo_id(requisicao, id_cliente):
    return Cliente.objects.get(id=id_cliente)

def obter_funcionario_ativo_pelo_id(requisicao, id_funcionario):
    return Funcionario.objects.get(id=id_funcionario)

def criar_agendamento(requisicao, servico, cliente, funcionario, data, hora, id_empresa):
    empresa = obter_empresa_por_id(requisicao, id_empresa)

    agendamento = Agendamento.objects.create(servico=servico, funcionario=funcionario, cliente=cliente, data=data, hora=hora, empresa=empresa)
    agendamento.save()

def criar_funcionario(requisicao, id_empresa, nome):
    empresa = obter_empresa_por_id(requisicao, id_empresa)

    funcionario = Funcionario.objects.create(nome = nome, empresa = empresa)
    
    funcionario.save()

def criar_cliente(requisicao, id_empresa, nome):
    empresa = obter_empresa_por_id(requisicao, id_empresa)

    cliente = Cliente.objects.create(nome = nome, empresa = empresa)

    cliente.save()

def criar_servico(requisicao, id_empresa, nome, descricao, preco):
    empresa = obter_empresa_por_id(requisicao, id_empresa)

    servico = Servico.objects.create(nome = nome, descricao = descricao, preco = preco, empresa = empresa)
    servico.save()

def atualizar_agendamento(requisicao, id_agendamento, servico, cliente, funcionario, data, hora):
    agendamento = obter_agendamento_ativo_pelo_id(requisicao, id_agendamento)

    agendamento.servico = servico
    agendamento.cliente = cliente
    agendamento.funcionario = funcionario
    
    if data == "" or data == None:
        data = agendamento.data
    
    if hora == "" or hora == None:
        hora = agendamento.hora
    
    agendamento.data = data
    agendamento.hora = hora
    agendamento.save()

def atualizar_funcionario(requisicao, id_funcionario, nome):
    funcionario = obter_funcionario_ativo_pelo_id(requisicao, id_funcionario)

    funcionario.nome = nome

    funcionario.save()

def atualizar_servico(requisicao, id_servico, nome, descricao, preco):
    servico = obter_servico_ativo_pelo_id(requisicao, id_servico)

    servico.nome = nome
    servico.descricao = descricao
    servico.preco = float(preco)

    servico.save()

def atualizar_cliente(requisicao, id_cliente, nome):
    cliente = obter_cliente_ativo_pelo_id(requisicao, id_cliente)

    cliente.nome = nome
    
    cliente.save()

def completar_agendamento(requisicao, id_agendamento):
    agendamento = obter_agendamento_ativo_pelo_id(requisicao, id_agendamento)

    agendamento.completo = True
    
    agendamento.save()

def deletar_servico(requisicao, id_servico):
    servico = obter_servico_ativo_pelo_id(requisicao, id_servico)

    deletar_objeto(requisicao, servico)

def deletar_funcionario(requisicao, id_funcionario):
    funcionario = obter_funcionario_ativo_pelo_id(requisicao, id_funcionario)

    deletar_objeto(requisicao, funcionario)

def deletar_cliente(requisicao, id_cliente):
    cliente = obter_cliente_ativo_pelo_id(requisicao, id_cliente)

    deletar_objeto(requisicao, cliente)

def deletar_agendamento(requisicao, id_agendamento):
    agendamento = obter_agendamento_ativo_pelo_id(requisicao, id_agendamento)

    deletar_objeto(requisicao, agendamento)

def deletar_objeto(requisicao, obj):
    obj.ativo = False
    obj.save()

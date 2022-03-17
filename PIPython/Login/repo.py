from Login.models import Empresa
from django.db import IntegrityError
from django.contrib import messages

def obter_empresa_por_id(requisicao, id_empresa):
    return Empresa.objects.get(id = id_empresa)

def atualizar_empresa(requisicao, id_empresa, nome_empresa, email_empresa, senha_empresa):
    empresa = obter_empresa_por_id(requisicao, id_empresa)

    empresa.nome = nome_empresa
    empresa.email = email_empresa

    if senha_empresa != "":
        empresa.set_password(senha_empresa)
    try:
        empresa.save()
        messages.success(requisicao, "Empresa alterada com sucesso.")
    except IntegrityError:
        messages.error(requisicao, "Empresa já cadastrada no sistema, por favor verifique o Email.")

def criar_empresa_usuario(requisicao, email, senha, cnpj_cpf, nome):
    Empresa.objects.create_user(username = email, email = email, password = senha, 
    cnpj_cpf = cnpj_cpf, nome = nome)
from Login.models import Empresa

def obter_empresa_por_id(requisicao, id_empresa):
    return Empresa.objects.get(id = id_empresa)

def atualizar_empresa(requisicao, id_empresa, nome_fantasia, email_empresa, senha_empresa):
    empresa = obter_empresa_por_id(requisicao, id_empresa)

    empresa.nome_fantasia = nome_fantasia
    empresa.email = email_empresa
    empresa.set_password(senha_empresa)
    
    empresa.save()

def criar_empresa_usuario(requisicao, email, senha, cnpj, nome_fantasia):
    Empresa.objects.create_user(username = email, email = email, password = senha, 
    cnpj = cnpj, nome_fantasia = nome_fantasia)
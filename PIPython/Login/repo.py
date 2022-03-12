from Login.models import Empresa

def obter_empresa_por_id(requisicao, id_empresa):
    return Empresa.objects.get(id = id_empresa)

def atualizar_empresa(requisicao, id_empresa, nome_empresa, email_empresa, senha_empresa):
    empresa = obter_empresa_por_id(requisicao, id_empresa)

    empresa.nome = nome_empresa
    empresa.email = email_empresa

    if senha_empresa != "":
        empresa.set_password(senha_empresa)
    
    empresa.save()

def criar_empresa_usuario(requisicao, email, senha, cnpj_cpf, nome):
    Empresa.objects.create_user(username = email, email = email, password = senha, 
    cnpj_cpf = cnpj_cpf, nome = nome)
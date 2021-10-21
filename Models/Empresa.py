from validate_docbr import CNPJ


class Empresa:
    def __init__(self, nomeFantasia, razaoSocial, cnpj, agendamentos, servicos, funcionarios, email, senha):
        self.Validar(nomeFantasia, razaoSocial, cnpj, agendamentos, servicos, funcionarios, email, senha)
        self.__nomeFantasia = nomeFantasia
        self.__razaoSocial = razaoSocial
        self.__cnpj__ = cnpj
        self.__agendamentos = agendamentos
        self.__servicos = servicos
        self.__funcionarios = funcionarios
        self.__email = email
        self.__senha = senha

    def Validar(self, nomeFantasia, razaoSocial, __cnpj__, agendamentos, servicos, funcionarios, email, senha):
        if not nomeFantasia or nomeFantasia.isspace():
            raise ValueError("Nome Fantasia da empresa invalido")
        if not razaoSocial or razaoSocial.isspace():
            raise ValueError("Razao Social da empresa invalida")
        if not __cnpj__ or __cnpj__.isspace() or not CNPJ().validate(__cnpj__):
            raise ValueError("CNPJ da empresa invalido")
        if not agendamentos:
            raise ValueError("Agendamento Invalido")
        if not servicos:
            raise ValueError("Servicos Invalidos")
        if not funcionarios:
            raise ValueError("funcionarios Invalidos")
        if not email or email.isspace():
            raise ValueError("Email da empresa invalido")
        if not senha or senha.isspace():
            raise ValueError("Senha da empresa invalida")

    @property
    def nomeFantasia(self):
        return self.__nomeFantasia

    @nomeFantasia.setter
    def nomeFantasia(self, nomeFantasia):
        self.__nomeFantasia = nomeFantasia

    @property
    def razaoSocial(self):
        return self.__razaoSocial

    @razaoSocial.setter
    def razaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial

    @property
    def cnpj(self):
        return self.__cnpj__

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj__ = cnpj

    @property
    def agendamentos(self):
        return self.__agendamentos

    @agendamentos.setter
    def agendamentos(self, agendamentos):
        self.__agendamentos = agendamentos

    @property
    def servicos(self):
        return self.__servicos

    @servicos.setter
    def servicos(self, servicos):
        self.__servicos = servicos

    @property
    def funcionarios(self):
        return self.__funcionarios

    @funcionarios.setter
    def funcionarios(self, funcionarios):
        self.__funcionarios = funcionarios

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

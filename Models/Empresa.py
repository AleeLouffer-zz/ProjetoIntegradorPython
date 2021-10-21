from validate_docbr import CNPJ


class Empresa:
    def __init__(self, nomeFantasia, razaoSocial, cnpj, email, senha):
        self.Validar(nomeFantasia, razaoSocial, cnpj, email, senha)
        self.__nomeFantasia = nomeFantasia
        self.__razaoSocial = razaoSocial
        self.__cnpj__ = cnpj
        self.__email = email
        self.__senha = senha

    @staticmethod
    def Validar(nomeFantasia, razaoSocial, cnpj, email, senha):
        if not nomeFantasia or nomeFantasia.isspace():
            raise ValueError("Nome Fantasia da empresa vazio ou nulo")
        if not razaoSocial or razaoSocial.isspace():
            raise ValueError("Razao Social da empresa vazio ou nulo")
        if not cnpj or cnpj.isspace() or not CNPJ().validate(cnpj):
            raise ValueError("CNPJ da empresa vazio ou nulo")
        if not email or email.isspace():
            raise ValueError("Email da empresa vazio ou nulo")
        if not senha or senha.isspace():
            raise ValueError("Senha da empresa vazio ou nulo")

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

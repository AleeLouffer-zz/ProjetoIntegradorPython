class Funcionario:
    def __init__(self, nome):
        self.Valida(nome)
        self.__Nome = nome

    def Valida(self, nome):
        if not nome or nome.isspace():
            raise ValueError("O Nome do Funcionario esta vazio ou nulo")

    @property
    def nome(self):
        return self.__Nome

    @nome.setter
    def nome(self, novo):
        self.__Nome = novo
        return self.__Nome

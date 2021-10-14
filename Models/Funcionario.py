class Funcionario:
    def __init__(self, nome):
        self.__Nome = nome

    @property
    def nome(self):
        return self.__Nome

    @nome.setter
    def nome(self, novo):
        self.__Nome = novo
        return self.__Nome

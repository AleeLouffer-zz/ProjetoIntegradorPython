class Cliente:
  def __init__(self, nome, telefone):
    self.validar(nome,telefone) 
    self.__Nome = nome
    self.__Telefone = telefone

  @property
  def Nome(self):
    return self.__Nome

  @Nome.setter
  def Nome(self, novoNome):
    self.__Nome = novoNome
    return self.__Nome

  @property
  def Telefone(self):
    return self.__Telefone

  @Telefone.setter
  def Telefone(self, novoTelefone):
    self.__Telefone = novoTelefone
    return self.__Telefone
  
  def validar(self, nome, telefone):
    if not nome or nome.isspace():
      raise ValueError("Nome Invalido")
    
    if not telefone or telefone.isspace():
      raise ValueError("Telefone Invalido")

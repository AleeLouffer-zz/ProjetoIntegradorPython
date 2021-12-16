class Agendamento:
  def __init__(self, servico, funcionario, cliente, empresa, dataEHora):
    self.validar_dados(servico, funcionario, cliente, empresa, dataEHora)
    self.__servico = servico
    self.__funcionario = funcionario
    self.__cliente = cliente
    self.__empresa = empresa
    self.__dataEHora = dataEHora
  
  def validar_dados (self, servico, funcionario, cliente, empresa, dataEHora):
    if not servico:
        raise ValueError("O agendamento precisa de um serviço válido")
    if not funcionario:
        raise ValueError("O agendamento precisa de um funcionário válido")
    if not cliente:
        raise ValueError("O agendamento precisa de um cliente válido")
    if not empresa:
        raise ValueError("O agendamento precisa de um empresa válido")
    if not dataEHora:
        raise ValueError("O agendamento precisa de um data e hora válido")

  @property
  def servico(self):
    return self.__servico

  @servico.setter
  def servico(self, servico):
    self.__servico = servico

  @property
  def funcionario(self):
    return self.__funcionario

  @funcionario.setter
  def funcionario(self, funcionario):
    self.__funcionario = funcionario

  @property
  def cliente(self):
    return self.__cliente

  @cliente.setter
  def cliente(self, cliente):
    self.__cliente = cliente

  @property
  def empresa(self):
    return self.__empresa

  @empresa.setter
  def empresa(self, empresa):
    self.__empresa = empresa

  @property
  def dataEHora(self):
    return self.__dataEHora

  @dataEHora.setter
  def dataEHora(self, dataEHora):
    self.__dataEHora = dataEHora

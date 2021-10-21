import unittest
from datetime import datetime
from Models.Agendamento import Agendamento
#Adicionar importação das classes de Servico, ....

class AgendamentoTeste(unittest.TestCase):
  def test_Deve_criar_um_agendamento(self):
    servico = Servico()
    funcionario = Funcionario()
    cliente = Cliente()
    empresa = Empresa()
    dataEHora = datetime.strptime('08/10/2021 09:22', '%d/%m/%Y %H:%M')
    agendamento = Agendamento(servico, funcionario,cliente, empresa, dataEHora)

    assert agendamento.servico == servico
    assert agendamento.funcionario == funcionario
    assert agendamento.cliente == cliente
    assert agendamento.empresa == empresa
    assert agendamento.dataEHora == dataEHora
  
  def test_Nao_deve_criar_um_agendamento_sem_servico(self):
    servico = Servico()
    funcionario = Funcionario()
    cliente = Cliente()
    empresa = Empresa()
    dataEHora = datetime.strptime('08/10/2021 09:22', '%d/%m/%Y %H:%M')
    with self.assertRaises(ValueError):  
      agendamento = Agendamento(None, funcionario, cliente, empresa, dataEHora)
      
  def test_Nao_deve_criar_um_agendamento_sem_funcionario(self):
     servico = Servico()
     cliente = Cliente()
     empresa = Empresa()
     dataEHora = datetime.strptime('08/10/2021 09:22', '%d/%m/%Y %H:%M')
     with self.assertRaises(ValueError):  
       agendamento = Agendamento(servico, None, cliente, empresa, dataEHora)
      
  def test_Nao_deve_criar_um_agendamento_sem_cliente(self):
     servico = Servico()
     funcionario = Funcionario()
     empresa = Empresa()
     dataEHora = datetime.strptime('08/10/2021 09:22', '%d/%m/%Y %H:%M')
     with self.assertRaises(ValueError):  
       agendamento = Agendamento(servico, funcionario, None, empresa, dataEHora)
      
  def test_Nao_deve_criar_um_agendamento_sem_empresa(self):
     servico = Servico()
     funcionario = Funcionario()
     cliente = Cliente()
     dataEHora = datetime.strptime('08/10/2021 09:22', '%d/%m/%Y %H:%M')
     with self.assertRaises(ValueError):  
       agendamento = Agendamento(servico, funcionario, cliente, None, dataEHora)
      
  def test_Nao_deve_criar_um_agendamento_sem_data_e_hora(self):
     servico = Servico()
     funcionario = Funcionario()
     cliente = Cliente()
     empresa = Empresa()
     with self.assertRaises(ValueError):  
       agendamento = Agendamento(servico, funcionario, cliente, empresa, None)
      


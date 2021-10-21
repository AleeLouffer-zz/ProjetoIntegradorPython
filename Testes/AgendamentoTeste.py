import unittest
from datetime import datetime
from Models.Agendamento import Agendamento
from Models.Servico import Servico
from Models.Cliente import Cliente
from Models.Funcionario import Funcionario
from Models.Empresa import Empresa


class AgendamentoTeste(unittest.TestCase):
    def setUp(self):
        self.servico = Servico("Corte de cabelo", "Corte Simples", 30, 1)
        self.funcionario = Funcionario("Cleide")
        self.cliente = Cliente("Claudia", "12345")
        self.empresa = Empresa("Dell", "DellComputadores", "06868396000170", "Dell@gmail.com", "EuOdeioPython")
        self.dataEHora = datetime.strptime('08/10/2021 09:22', '%d/%m/%Y %H:%M')

    def test_Deve_criar_um_agendamento(self):
        agendamento = Agendamento(self.servico, self.funcionario, self.cliente, self.empresa, self.dataEHora)

        assert agendamento.servico == self.servico
        assert agendamento.funcionario == self.funcionario
        assert agendamento.cliente == self.cliente
        assert agendamento.empresa == self.empresa
        assert agendamento.dataEHora == self.dataEHora

    def test_Nao_deve_criar_um_agendamento_sem_servico(self):
        with self.assertRaises(ValueError):
            agendamento = Agendamento(None, self.funcionario, self.cliente, self.empresa, self.dataEHora)

    def test_Nao_deve_criar_um_agendamento_sem_funcionario(self):
        with self.assertRaises(ValueError):
            agendamento = Agendamento(self.servico, None, self.cliente, self.empresa, self.dataEHora)

    def test_Nao_deve_criar_um_agendamento_sem_cliente(self):
        with self.assertRaises(ValueError):
           agendamento = Agendamento(self.servico, self.funcionario, None, self.empresa, self.dataEHora)

    def test_Nao_deve_criar_um_agendamento_sem_empresa(self):
        with self.assertRaises(ValueError):
            agendamento = Agendamento(self.servico, self.funcionario, self.cliente, None, self.dataEHora)

    def test_Nao_deve_criar_um_agendamento_sem_data_e_hora(self):
        with self.assertRaises(ValueError):
            agendamento = Agendamento(self.servico, self.funcionario, self.cliente, self.empresa, None)
            agendamento = Agendamento(self.servico, self.funcionario, self.cliente, self.empresa, "    ")



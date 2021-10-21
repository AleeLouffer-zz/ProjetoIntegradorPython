import unittest
from Models.Empresa import Empresa


class TesteEmpresa(unittest.TestCase):
    def test_Deve_criar_uma_empresa(self):
        empresa = Empresa("Dell", "DellComputadores", "06868396000170", "agendamentos", "servicos", "funcionarios", "Dell@gmail.com", "EuOdeioPython")
        assert empresa.nomeFantasia == "Dell"
        assert empresa.razaoSocial == "DellComputadores"
        assert empresa.cnpj == "06868396000170"
        assert empresa.agendamentos == "agendamentos"
        assert empresa.servicos == "servicos"
        assert empresa.funcionarios == "funcionarios"
        assert empresa.email == "Dell@gmail.com"
        assert empresa.senha == "EuOdeioPython"

    def test_Nao_deve_criar_uma_empresa_com_nome_invalido(self):
        with self.assertRaises(ValueError):
            empresa = Empresa(None, "DellComputadores", "21032193210", "agendamentos", "servicos", "funcionarios",
                          "Dell@gmail.com", "EuOdeioPython")

    def test_Nao_deve_criar_uma_empresa_com_razao_social_invalida(self):
        with self.assertRaises(ValueError):
            empresa = Empresa("Dell", None, "21032193210", "agendamentos", "servicos", "funcionarios", "Dell@gmail.com", "EuOdeioPython")

    def test_Nao_deve_criar_uma_empresa_com_CNPJ_vazio(self):
        with self.assertRaises(ValueError):
            empresa = Empresa("Dell", "DellComputadores", None, "agendamentos", "servicos", "funcionarios", "Dell@gmail.com", "EuOdeioPython")

    def test_Nao_deve_criar_uma_empresa_com_CNPJ_invalido(self):
        with self.assertRaises(ValueError):
            empresa = Empresa("Dell", "DellComputadores", "89493000117", "agendamentos", "servicos", "funcionarios", "Dell@gmail.com", "EuOdeioPython")


    def test_Nao_deve_criar_uma_empresa_com_agendamentos_invalidos(self):
        with self.assertRaises(ValueError):
            empresa = Empresa("Dell", "DellComputadores", "21032193210", None, "servicos", "funcionarios", "Dell@gmail.com", "EuOdeioPython")

    def test_Nao_deve_criar_uma_empresa_com_servicos_invalidos(self):
        with self.assertRaises(ValueError):
            empresa = Empresa("Dell", "DellComputadores", "21032193210", "agendamentos", None, "funcionarios", "Dell@gmail.com", "EuOdeioPython")

    def test_Nao_deve_criar_uma_empresa_com_funcionarios_invalidos(self):
        with self.assertRaises(ValueError):
            empresa = Empresa("Dell", "DellComputadores", "21032193210", "agendamentos", "servicos", None, "Dell@gmail.com", "EuOdeioPython")

    def test_Nao_deve_criar_uma_empresa_com_email_invalido(self):
        with self.assertRaises(ValueError):
            empresa = Empresa("Dell", "DellComputadores", "21032193210", "agendamentos", "servicos", "funcionarios", None, "EuOdeioPython")

    def test_Nao_deve_criar_uma_empresa_com_senha(self):
        with self.assertRaises(ValueError):
            empresa = Empresa("Dell", "DellComputadores", "21032193210", "agendamentos", "servicos", "funcionarios", "Dell@gmail.com", None)


if __name__ == '__main__':
    unittest.main()

import unittest
from Models.Empresa import Empresa


class TesteEmpresa(unittest.TestCase):
    nomeFantasia = "Dell"
    razaoSocial = "DellComputadores"
    cnpj = "06868396000170"
    email = "Dell@gmail.com"
    senha = "EuOdeioPython"

    def test_Deve_criar_uma_empresa(self):
        empresa = Empresa("Dell", "DellComputadores", "06868396000170", "Dell@gmail.com", "EuOdeioPython")
        assert empresa.nomeFantasia == "Dell"
        assert empresa.razaoSocial == "DellComputadores"
        assert empresa.cnpj == "06868396000170"
        assert empresa.email == "Dell@gmail.com"
        assert empresa.senha == "EuOdeioPython"

    def test_Nao_deve_criar_uma_empresa_com_nome_vazio_ou_nulo(self):
        with self.assertRaises(ValueError):
            empresa = Empresa(None, self.razaoSocial, self.cnpj, self.email, self.senha)

    def test_Nao_deve_criar_uma_empresa_com_razao_social_vazio_ou_nulo(self):
        with self.assertRaises(ValueError):
            empresa = Empresa(self.nomeFantasia, None, self.cnpj, self.email, self.senha)

    def test_Nao_deve_criar_uma_empresa_com_CNPJ_vazio_ou_nulo(self):
        with self.assertRaises(ValueError):
            empresa = Empresa(self.nomeFantasia, self.razaoSocial, None, self.email, self.senha)

    def test_Nao_deve_criar_uma_empresa_com_CNPJ_invalido(self):
        cnpjInvalido = "89493000117"
        with self.assertRaises(ValueError):
            empresa = Empresa(self.nomeFantasia, self.razaoSocial, cnpjInvalido, self.email, self.senha)

    def test_Nao_deve_criar_uma_empresa_com_email_vazio_ou_nulo(self):
        with self.assertRaises(ValueError):
            empresa = Empresa(self.nomeFantasia, self.razaoSocial, self.cnpj, None, self.senha)

    def test_Nao_deve_criar_uma_empresa_com_vazio_ou_nulo(self):
        with self.assertRaises(ValueError):
            empresa = Empresa(self.nomeFantasia, self.razaoSocial, self.cnpj, self.email, None)


if __name__ == '__main__':
    unittest.main()

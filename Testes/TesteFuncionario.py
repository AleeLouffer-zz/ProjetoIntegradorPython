from Models.Funcionario import Funcionario
import unittest


class TesteFuncionario(unittest.TestCase):

    def test_Deve_criar_um_funcionario_com_nome(self):
        funcionario = Funcionario("Fulano")
        assert funcionario.nome == "Fulano"

    def test_Nao_deve_criar_um_funcionario_sem_nome(self):
        with self.assertRaises(ValueError):
            funcionario = Funcionario("")


if __name__ == '__main__':
    unittest.main()

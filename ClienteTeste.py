import unittest
from Cliente import * 


class TesteFuncionario(unittest.TestCase):
   def test_deve_criar_um_cliente(self):
    cliente = Cliente("kaique","12345")
  
    assert cliente.Nome == "kaique"
    assert cliente.Telefone == "12345"
   
   def test_nao_deve_criar_um_cliente_com_nome_invalido(self):
    with self.assertRaises(ValueError):  
      cliente = Cliente("","12345")
   
   def test_nao_deve_criar_um_cliente_com_telefone_invalido(self):
    with self.assertRaises(ValueError):  
      cliente = Cliente("Kaique","")

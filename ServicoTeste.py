from Servico import Servico
import unittest


class TesteServico(unittest.TestCase):
  def test_Deve_criar_um_servico_valido(self):
    nome = "Corte de Cabelo"
    descricao = "Corte Simples"
    preco = 15
    id_empresa = 102
    servico = Servico(nome, descricao , preco, id_empresa)
    assert servico.nome == nome
    assert servico.descricao == descricao
    assert servico.preco == preco
    assert servico.id_empresa == id_empresa
    
  def test_Nao_deve_criar_um_servico_sem_nome(self):
    with self.assertRaises(ValueError):  
      servico = Servico(None, "Corte Simples", 15, 102)
      
  def test_Nao_deve_criar_um_servico_sem_descricao(self):
    with self.assertRaises(ValueError):  
      servico = Servico("Corte Simples", None, 15, 102)  
      
  def test_Nao_deve_criar_um_servico_com_preco_invalido(self):
    with self.assertRaises(ValueError):  
      servico = Servico("Corte de Cabelo", "Corte Simples", -15, 102)  
      
  def test_Nao_deve_criar_um_servico_com_id_da_empresa_invalido (self):
    with self.assertRaises(ValueError):  
      servico = Servico("Corte de Cabelo", "Corte Simples", 15, 0)    

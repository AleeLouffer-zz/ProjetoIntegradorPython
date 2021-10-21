class Servico:
    def __init__ (self, nome, descricao, preco, id_empresa):
        self.Validar (nome, descricao, preco, id_empresa)
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.id_empresa = id_empresa
        
    def Validar(self, nome, descricao, preco, id_empresa):      
      if not nome or (nome.isspace()):
        raise ValueError("O campo nome deve ser preenchido.")
  

      if not descricao or (descricao.isspace()):
        raise ValueError("O campo descrição deve ser preenchida.")
        

      if not preco or (preco <= 0):
        raise ValueError("O campo preço deve ser preenchido com valores válidos.")
      


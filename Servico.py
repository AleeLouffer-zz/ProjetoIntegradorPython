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

      print(nome)  

      if not descricao or (descricao.isspace()):
        raise ValueError("O campo descrição deve ser preenchida.")

      print(descricao) 

      if not preco or (preco <= 0):
        raise ValueError("O campo preço deve ser preenchido com valores válidos.")
      
      print(preco)

      if not id_empresa or (id_empresa <= 0):
        raise ValueError("O campo id da empresa deve ser preenchido com valores válidos.")

      print(id_empresa)

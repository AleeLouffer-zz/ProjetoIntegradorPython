from django.db import models
from Login.models import Empresa

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
  
class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    preco = models.FloatField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
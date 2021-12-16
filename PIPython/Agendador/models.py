from django.db import models

class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    servico = models.ForeignKey('Servico', on_delete=models.CASCADE)
    funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    dataEHora = models.DateField(null=True)
  

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 11)


class Empresa(models.Model):      
    id = models.AutoField(primary_key=True)
    razaoSocial = models.CharField(max_length=100)
    cnpj = models.IntegerField(max_length=15)
    email = models.CharField(max_length=40)
    senha = models.CharField(max_length=20)


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 100)

  
class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    preco = models.FloatField()
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)

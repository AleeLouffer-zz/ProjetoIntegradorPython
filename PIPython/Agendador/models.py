from django.db import models
from django import forms

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
    razao_social = models.CharField(max_length=100, null=True)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.IntegerField(unique=True)
    email = models.CharField(max_length=40)
    senha = models.CharField(max_length=20)

    def salvar_no_banco(self, razao_social):
        self.razao_social = razao_social
        self.save()


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 100)

  
class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    preco = models.FloatField()
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)

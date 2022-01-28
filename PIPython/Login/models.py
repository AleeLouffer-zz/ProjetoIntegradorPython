from django.db import models

class Empresa(models.Model):      
    id = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=100, null=True)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.IntegerField(unique=True)
    email = models.CharField(max_length=40)
    senha = models.CharField(max_length=20)

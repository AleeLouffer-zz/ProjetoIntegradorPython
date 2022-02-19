from django.db import models
from Agendador.models import Agendamento
from Login.models import Empresa

class Forma_de_Pagamento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ativo = models.BooleanField(null=False, default=True)

class Contas_a_Receber(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.FloatField()
    pago = models.BooleanField(null=False, default=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    data_de_pagamento = models.DateField(null=True)
    data_de_vencimento = models.DateField()
    data_de_emissao = models.DateField(auto_now_add=True)
    forma_de_pagamento = models.ForeignKey(Forma_de_Pagamento, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    ativo = models.BooleanField(null=False, default=True)



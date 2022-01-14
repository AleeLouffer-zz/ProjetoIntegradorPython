import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from Login.models import Empresa

def tela_inicial_prestador(requisicao, id_empresa):
    empresa = Empresa.objects.get(id=id_empresa)

    if empresa.is_valid():
        return render(requisicao, '#tela inicial', empresa)
import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

def tela_inicial_prestador(requisicao):
    return render(requisicao, '../templates/telaPrestador.html')


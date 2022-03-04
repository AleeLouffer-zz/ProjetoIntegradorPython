from django.shortcuts import redirect, render
from Agendador.views import *
from django.contrib.auth import authenticate, login
from Agendador.views import *
from Login.repo import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from Login.models import Empresa
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def tela_login(requisicao):
    return render(requisicao, '../templates/login/login.html')

def renderizar_tela_cadastro(requisicao):
    return render(requisicao, 'telaCadastro.html')

def cadastrar_empresa(requisicao):
    razao_social = requisicao.POST['razao_social_cadastro']
    nome_fantasia = requisicao.POST['nome_cadastro']
    cnpj = requisicao.POST['cnpj_cadastro']
    email = requisicao.POST['email_cadastro']
    senha = requisicao.POST['senha_cadastro']

    criar_empresa_usuario(requisicao, email, senha, cnpj, nome_fantasia, razao_social)

    return redirect('Login:tela_login')
  
def realizar_login(requisicao):
    email = requisicao.POST['email']
    senha = requisicao.POST['senha']
    
    user = authenticate(requisicao, username=email, password=senha)

    empresa = obter_empresa_por_id(requisicao, user.id)

    if user is not None:
        if user.is_active:
            login(requisicao, user)
            requisicao.session["id_empresa"] = user.id
            requisicao.session["nome_empresa"] = empresa.nome_fantasia
            return redirect("/empresa/")
        
    else:
        return redirect('Login:tela_login')
    
def editar_empresa(requisicao):
    id_empresa = requisicao.session["id_empresa"]
    nome_empresa = requisicao.POST['nome_empresa']
    email_empresa = requisicao.POST['email_empresa']
    senha_empresa = requisicao.POST['senha_empresa']

    atualizar_empresa(requisicao, id_empresa, nome_empresa, email_empresa, senha_empresa)

    return redirect('tela_inicial_prestador')

def requisicao_de_redefinicao_de_senha(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = Empresa.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Email para Trocar de Senha - Agendador Senac - MS"
					email_template_name = "../templates/esqueci_senha/texto_esqueci_senha.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Agendador Senac - MS',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("Login:redefinir_senha_sucesso")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="../templates/esqueci_senha/resetar_senha.html", context={"password_reset_form":password_reset_form})

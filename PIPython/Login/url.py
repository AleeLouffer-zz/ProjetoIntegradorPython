from django.urls import path, reverse_lazy
from Login import views
from django.contrib.auth import views as auth_views

app_name = 'Login'

urlpatterns = [
    path('cadastrar/', views.renderizar_tela_cadastro, name="cadastro_empresa"),
    path('cadastrar_empresa/', views.cadastrar_empresa, name="cadastrar_empresa"),
    path("", views.tela_login, name="tela_login"),
    path("login/", views.realizar_login, name="realizar_login"),
    path('editar_empresa/', views.editar_empresa, name="editarEmpresa"),
    path("redefinir_senha", views.requisicao_de_redefinicao_de_senha, name="redefinir_senha"),
    path('redefinir_senha_sucesso/', auth_views.PasswordResetDoneView.as_view(template_name="../templates/esqueci_senha/resetar_senha_sucesso.html"), name="redefinir_senha_sucesso"),
    path('redefinir_senha/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="../templates/esqueci_senha/confirmacao_esqueci_senha.html", success_url = reverse_lazy('Login:redefinir_senha_completo')), name="confirmacao_esqueci_senha"),
    path('redefinir_senha_completo/', auth_views.PasswordResetCompleteView.as_view(template_name="../templates/esqueci_senha/resetar_senha_completo.html"), name="redefinir_senha_completo"),
]

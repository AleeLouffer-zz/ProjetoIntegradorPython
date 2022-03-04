from django.urls import path, include

urlpatterns = [
    path('', include('Login.url')),
    path('', include('Agendador.url')),
    path('', include('Contas_a_Receber.url')),
]

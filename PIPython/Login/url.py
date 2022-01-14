from django.contrib import admin
from django.urls import path
from Login import views


urlpatterns = [
    path('index/', views.Tela_Inicial, name="tela_inicial"),
    path('entrar/', views.Entrar, name="entrar")
]

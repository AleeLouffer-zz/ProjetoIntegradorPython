from django.contrib import admin
from django.urls import path
from Login import views

appname = "Agendador"
urlpatterns = [
    path('empresa/', views.tela_inicial_prestador, name="tela_inicial_prestador"),
]

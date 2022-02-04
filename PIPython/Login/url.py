from django.contrib import admin
from django.urls import path
from Login import views


urlpatterns = [
    path("login/", views.tela_login, name="tela_login"),
    path("login/entrar", views.realizar_login, name="realizar_login"),
]

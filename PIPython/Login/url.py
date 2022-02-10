from django.contrib import admin
from django.urls import path
from Login import views


urlpatterns = [
    path("", views.tela_login, name="tela_login"),
    path("login", views.realizar_login, name="realizar_login"),
]

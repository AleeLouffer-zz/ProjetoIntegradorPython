from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Login.url')),
    path('', include('Agendador.url')),
]

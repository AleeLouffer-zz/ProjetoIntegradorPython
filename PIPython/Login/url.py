from django.contrib import admin
from django.urls import path
from Login import views

urlpatterns = [
    path('contasAReceber/',views.contas_a_receber, name="contas_a_receber"),
    path('agenda/', views.agenda_prestador, name= "agenda_prestador"),
]

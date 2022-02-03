from django.contrib import admin
from django.urls import path
from Agendador import views

app_name="agendador"

urlpatterns = [
    path('agenda/<int:id_empresa>/', views.tela_agenda, name="tela_agenda"),
    path('agenda/filtros_agenda', views.filtros_agenda, name="filtros_agenda"),
    path('agenda/adicionar_agendamento/', views.tela_adicionar_agendamento, name="tela_adicionar_agendamento"),
    path('agenda/add_agendamento', views.adicionar_agendamento, name="adicionar_agendamento"),
    path('agenda/verifica_botoes_agendamento', views.verifica_botoes_agendamento, name="verifica_botoes_agendamento"),
    path('agenda/editar_agendamento', views.editar_agendamento, name="editar_agendamento")
]

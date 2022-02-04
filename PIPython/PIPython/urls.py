from django.contrib import admin
from django.urls import path, include
from Agendador import views

urlpatterns = [
    path('', include('Agendador.url')),
    path('admin/', admin.site.urls),
]

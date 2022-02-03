from django.contrib import admin
from django.urls import path, include
from Agendador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agendador/', include('Agendador.url'))
]

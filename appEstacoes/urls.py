from django.urls import path
from .views import lista_estacoes

urlpatterns = [
    path('lista/', lista_estacoes, name='lista_estacoes'),
]
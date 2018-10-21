from django.urls import path
from .views import lista_leituras

urlpatterns = [
    path('lista/', lista_leituras, name='lista_leituras'),
]
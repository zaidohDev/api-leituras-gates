from django.urls import path
from .views import lista_gates

urlpatterns = [
    path('lista/', lista_gates, name='lista_gates'),
]
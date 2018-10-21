"""metrofor_gesop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from appEstacoes import urls as urls_estacoes
from appGates import urls as urls_gates
from appLeituras import urls as urls_leituras
from appEstacoes.api.viewsets import EstacaoViewSet
from appLeituras.api.viewsets import LeituraViewSet
from appGates.api.viewsets import GateViewSet

router = routers.DefaultRouter()
router.register('api-estacoes', EstacaoViewSet, base_name='Estacao')
router.register('api-leituras', LeituraViewSet, base_name='Leitura')
router.register('api-gates', GateViewSet, base_name='Gate')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('estacoes/', include(urls_estacoes)),
    path('gates/', include(urls_gates)),
    path('leituras', include(urls_leituras)),
]

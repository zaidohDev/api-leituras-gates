from rest_framework.viewsets import ModelViewSet
from appEstacoes.api.serializers import EstacaoSerializer
from appEstacoes.models import Estacao


class EstacaoViewSet(ModelViewSet):
    serializer_class = EstacaoSerializer

    def get_queryset(self):
        return Estacao.objects.filter(ativo=True)
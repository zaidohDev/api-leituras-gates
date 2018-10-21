from rest_framework.viewsets import ModelViewSet
from appLeituras.api.serializers import LeituraSerializer
from appLeituras.models import Leitura


class LeituraViewSet(ModelViewSet):
    serializer_class = LeituraSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        estacoes = self.request.query_params.get('estacoes', None)
        queryset = Leitura.objects.all()
        if id:
            queryset = Leitura.objects.filter(pk=id)
        if estacoes:
            queryset = queryset.filter(estacoes=estacoes)

        return queryset


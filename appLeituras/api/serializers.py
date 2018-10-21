from rest_framework.serializers import ModelSerializer
from appLeituras.models import Leitura


class LeituraSerializer(ModelSerializer):
    class Meta:
        model = Leitura
        fields = ('id', 'estacoes', 'gates', 'leitura_entrada', 'leitura_saida', 'ativa','created_at')
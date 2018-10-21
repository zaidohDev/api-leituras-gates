from rest_framework.serializers import ModelSerializer
from appEstacoes.models import Estacao


class EstacaoSerializer(ModelSerializer):
    class Meta:
        model = Estacao
        fields = ('id', 'nome', 'user', 'observacao', 'ativo', 'created_at')

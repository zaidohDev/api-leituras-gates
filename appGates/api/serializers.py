from rest_framework.serializers import ModelSerializer

from appGates.models import Gate


class GateSerializer(ModelSerializer):
    class Meta:
        model = Gate
        fields = ('id', 'nome', 'ativo', 'created_at')

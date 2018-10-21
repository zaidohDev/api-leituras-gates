from rest_framework.viewsets import ModelViewSet
from appGates.api.serializers import GateSerializer
from appGates.models import Gate


class GateViewSet(ModelViewSet):

    serializer_class = GateSerializer

    def get_queryset(self):
        return Gate.objects.filter(ativo=True)

from rest_framework import viewsets

from fantasy_sports.serializers import PlayerSerializer
from fantasy_sports.models import Player


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

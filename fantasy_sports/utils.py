import logging

from django.contrib.auth import get_user_model

from fantasy_sports.models import (FantasyLeague,
                                   Player,
                                   PlayerFantasyTeamXRef)
User = get_user_model()
logger = logging.getLogger('fantasy_sports')


def initialize_fantasy_league(commissioner: User, name: str, num_teams: int = 8) -> FantasyLeague:
    league = FantasyLeague(commissioner=commissioner,
                           name=name,
                           num_teams=num_teams)

    xrefs = []
    for player in Player.objects.all():
        xrefs.append(PlayerFantasyTeamXRef(league=league,
                                           team=None,
                                           player=player))
    PlayerFantasyTeamXRef.objects.bulk_create(xrefs)

    return league

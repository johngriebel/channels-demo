import logging

from typing import Dict
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


def parse_player_dict(input_data: Dict) -> Player:
    logger.info(f'Attempting to parse info for {input_data["PLAYER_ID"]}/{input_data["PLAYER_NAME"]}')
    data = {}
    full_name = input_data.pop('PLAYER_NAME')
    try:
        first_name, last_name = full_name.split(" ")
    except ValueError:
        first_name = None
        last_name = full_name
    data['first_name'] = first_name
    data['last_name'] = last_name
    data['nba_team_id'] = input_data.pop('TEAM_ID')
    data['nba_team_abbreviation'] = input_data.pop('TEAM_ABBREVIATION')
    data['wins'] = input_data.pop('W')
    data['losses'] = input_data.pop('L')

    player_fields = [f.name for f in Player._meta.get_fields()]
    for field in input_data:
        if field.lower() in player_fields:
            data[field.lower()] = input_data[field]

    player = Player(**data)
    player.save()
    return player

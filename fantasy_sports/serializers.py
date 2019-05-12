from rest_framework import serializers

from fantasy_sports.models import (Player,
                                   FantasyLeague,
                                   FantasyTeam,
                                   DraftPick)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'player_id', 'first_name', 'last_name', 'nba_team_id',
                  'nba_team_abbreviation', 'age', 'gp', 'wins', 'losses',
                  'min', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct',
                  'ftm', 'fta', 'ft_pct', 'oreb', 'dreb', 'reb', 'ast',
                  'tov', 'stl', 'blk', 'blka', 'pf', 'pfd', 'pts', 'plus_minus')


class FantasyLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyLeague
        fields = ('id', 'created_timestamp', 'updated_timestamp', 'commissioner',
                  'num_teams', 'name')
        read_only_fields = ('id', 'created_timestamp', 'updated_timestamp')


class FantasyTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyTeam
        fields = ('id', 'created_timestamp', 'updated_timestamp', 'fantasy_leage',
                  'owner', 'name')
        read_only_fields = ('id', 'created_timestamp', 'updated_timestamp')


class DraftPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftPick
        fields = ('created_timestamp', 'team', 'player', 'round', 'pick')
        read_only_fields = ('created_timestamp',)
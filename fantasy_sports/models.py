from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class ChannelsDemoBaseModel(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Player(ChannelsDemoBaseModel):
    player_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    nba_team_id = models.IntegerField(null=True)
    nba_team_abbreviation = models.CharField(max_length=5, blank=True, null=True)
    age = models.DecimalField(max_digits=3, decimal_places=1)
    gp = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    min = models.DecimalField(max_digits=3, decimal_places=1)
    fgm = models.DecimalField(max_digits=3, decimal_places=1)
    fga = models.DecimalField(max_digits=3, decimal_places=1)
    fg_pct = models.DecimalField(max_digits=4, decimal_places=3)
    fg3m = models.DecimalField(max_digits=3, decimal_places=1)
    fg3a = models.DecimalField(max_digits=3, decimal_places=1)
    fg3_pct = models.DecimalField(max_digits=4, decimal_places=3)
    ftm = models.DecimalField(max_digits=3, decimal_places=1)
    fta = models.DecimalField(max_digits=3, decimal_places=1)
    ft_pct = models.DecimalField(max_digits=4, decimal_places=3)
    oreb = models.DecimalField(max_digits=3, decimal_places=1)
    dreb = models.DecimalField(max_digits=3, decimal_places=1)
    reb = models.DecimalField(max_digits=3, decimal_places=1)
    ast = models.DecimalField(max_digits=3, decimal_places=1)
    tov = models.DecimalField(max_digits=3, decimal_places=1)
    stl = models.DecimalField(max_digits=3, decimal_places=1)
    blk = models.DecimalField(max_digits=3, decimal_places=1)
    blka = models.DecimalField(max_digits=3, decimal_places=1)
    pf = models.DecimalField(max_digits=3, decimal_places=1)
    pfd = models.DecimalField(max_digits=3, decimal_places=1)
    pts = models.DecimalField(max_digits=3, decimal_places=1)
    plus_minus = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        db_table = 'players'


class FantasyLeague(ChannelsDemoBaseModel):
    commissioner = models.ForeignKey(User, on_delete=models.CASCADE)
    num_teams = models.IntegerField()
    name = models.CharField(max_length=100, default='')
    # Probably other stuff...

    class Meta:
        db_table = 'fantasy_league'


class FantasyTeam(ChannelsDemoBaseModel):
    fantasy_league = models.ForeignKey(FantasyLeague, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'fantasy_team'


class PlayerFantasyTeamXRef(ChannelsDemoBaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(FantasyTeam, null=True, on_delete=models.CASCADE)
    league = models.ForeignKey(FantasyLeague, on_delete=models.CASCADE)

    class Meta:
        db_table = 'player_fantasy_team_xref'


class DraftPick(ChannelsDemoBaseModel):
    team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    round = models.IntegerField()
    pick = models.IntegerField()

    class Meta:
        db_table = 'draft_pick'

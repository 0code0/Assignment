from django.db import models

# Create your models here.


class Matches(models.Model):
    season = models.IntegerField(default=2000)
    city = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    date = models.DateField()
    team1 = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    team2 = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    toss_winner = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    toss_decision = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    result = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    dl_applied = models.BooleanField(default=False)
    winner = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    win_by_runs = models.IntegerField(default=0)
    win_by_wickets = models.IntegerField(default=0)
    player_of_match = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    venue = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    umpire1 = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    umpire2 = models.CharField(
        default=None, max_length=225, blank=True, null=True)
    umpire3 = models.CharField(
        default=None, max_length=225, blank=True, null=True)


class Deliveries(models.Model):
    match_id = models.IntegerField(default=1)
    inning	= models.IntegerField(default=1, )
    batting_team = models.CharField(default=None, max_length=22)	
    bowling_team	= models.CharField(default=None, max_length=22)
    over= models.IntegerField(default=1)	
    ball	= models.IntegerField(default=1)
    batsman	= models.CharField(default=None, max_length=22)
    non_striker	= models.CharField(default=None, max_length=22)
    bowler	= models.CharField(default=None, max_length=22)
    is_super_over	= models.BooleanField(default=False)
    wide_runs = models.IntegerField(default=0)
    bye_runs	= models.IntegerField(default=1)
    legbye_runs	= models.IntegerField(default=1)
    noball_runs	= models.IntegerField(default=1)
    penalty_runs	= models.IntegerField(default=1)
    batsman_runs	= models.IntegerField(default=1)
    extra_runs	= models.IntegerField(default=1)
    total_runs	= models.IntegerField(default=1)
    player_dismissed =	models.CharField(default=None, max_length=22, null=True, blank=True)
    dismissal_kind =	models.CharField(default=None, max_length=22, null=True, blank=True)
    fielder = models.CharField(default=None, max_length=22, null=True, blank=True)

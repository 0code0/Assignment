from django.shortcuts import render
from django.views import View
# Create your views here.
from gale.models import Matches
from django.db.models import Count, Sum, Max
from django.http import JsonResponse


class Index(View):

    def get(self, request):
        # Top 4 teams in terms of wins

        top4winner = self.top_4_teams()
        # Which team won the most number of tosses in the season
        tosses_result = self.team_won_most()

        # Which player won the maximum number of Player of the Match awards in the whole season
        playerofmatch = self.player_of_match()

        # Which team won max matches in the whole season

        winner = self.team_won_max_matches()

        # Which location has the most number of wins for the top team
        top4winnerlocation = self.location_max_wins()

        # Which % of teams decided to bat when they won the toss
        percentage_team = self.percentage_team_bat()

        # Which location hosted most number of matches
        most_number = self.location_hosted_most_matches()

        # Which team won by the highest margin of runs  for the season
        topwinner = self.highest_margin_runs()

        context = {
            "top4winner": top4winner,
            "tosses": tosses_result,
            "playerofmatch": playerofmatch,
            "winner": winner,
            "top4winnerlocation": top4winnerlocation,
            "per": percentage_team,
            "most_number": most_number,
            "topwinner": topwinner
        }

        return JsonResponse(context)

    def top_4_teams(self):
        top4winner = Matches.objects.values("winner").annotate(
            winners=Count("winner")).order_by("-winners")[:4]

        top4winner = [obj for obj in top4winner]
        return top4winner

    def team_won_most(self):
        tosses = Matches.objects.values("toss_winner", "season").annotate(
            toss=Count("toss_winner")).order_by("-season", "-toss")

        season_set = set()
        for t in tosses:
            season_set.add(t["season"])

        list_set = list(season_set)
        list_set.sort(reverse=True)

        tosses_result = []

        for l in list_set:
            filter_result = tosses.filter(season=l)
            temp = {"year": l, "name": filter_result[0]["toss_winner"], "count": filter_result.aggregate(Max("toss"))[
                "toss__max"]}
            tosses_result.append(temp)

        return tosses_result

    def player_of_match(self):

        playerofmatch = Matches.objects.values("player_of_match").annotate(
            match=Count("player_of_match")).order_by("-match")

        return playerofmatch[0]

    def team_won_max_matches(self):
        winner = Matches.objects.values("winner").annotate(
            winners=Count("winner")).order_by("-winners")
        return winner[0]

    def location_max_wins(self):
        top4winnerlocation = Matches.objects.values("winner", "city").annotate(
            winners=Count("winner")).order_by("-winners")[:4]

        top4winnerlocation = [obj for obj in top4winnerlocation]
        return top4winnerlocation

    def percentage_team_bat(self):
        tosses_won_bat = Matches.objects.values(
            "toss_winner", "toss_decision").annotate(toss=Count("toss_winner"))
        bat_won = 0
        field_won = 0
        for x in range(0, len(tosses_won_bat) - 1, 2):
            bat_won += tosses_won_bat[x]["toss"]
            field_won += tosses_won_bat[x+1]["toss"]
            # print(tosses_won_bat[x]["toss_winner"], tosses_won_bat[x]["toss_decision"], tosses_won_bat[x]["toss"])
        total = bat_won+field_won
        percentage_team = (bat_won/total)*100

        return percentage_team

    def location_hosted_most_matches(self):
        most_number = Matches.objects.values("venue").annotate(
            venues=Count("venue")).order_by("-venues")[0]

        return most_number

    def highest_margin_runs(self):
        topwinner = Matches.objects.values("winner", "season").annotate(
            runs=Sum("win_by_runs")).order_by("-runs")

        season_set = set()
        for t in topwinner:

            season_set.add(t["season"])
        list_set = list(season_set)
        list_set.sort(reverse=True)

        result = []

        for l in list_set:
            filter_result = topwinner.filter(season=l)
            temp = {"year": l, "name": filter_result[0]["winner"], "count": filter_result.aggregate(Max("runs"))[
                "runs__max"]}

            result.append(temp)

        return result

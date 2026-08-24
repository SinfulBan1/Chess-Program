from datetime import datetime

from .base import BaseCommand
from .context import Context
from models import TournamentManager


class TournamentStartCmd(BaseCommand):

    def execute(self):
        tm = TournamentManager()

        today = datetime.today().date()
        active_tournaments = []

        for tournament in tm.tournaments:
            start_date = datetime.strptime(
                tournament.dates["from"],
                "%d-%m-%Y"
            ).date()

            end_date = datetime.strptime(
                tournament.dates["to"],
                "%d-%m-%Y"
            ).date()

            if start_date <= today <= end_date:
                active_tournaments.append(tournament)

        if len(active_tournaments) == 1:
            return Context(
                "tournament-view",
                tournament=active_tournaments[0]
            )

        return Context(
            "tournament-list",
            tournaments=tm.tournaments
        )

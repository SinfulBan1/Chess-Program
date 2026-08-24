from .base import BaseCommand
from .context import Context
from models.tournament_manager import TournamentManager


class TournamentListCmd(BaseCommand):

    def execute(self):
        tm = TournamentManager()

        return Context(
            "tournament-list",
            tournaments=tm.tournaments
        )
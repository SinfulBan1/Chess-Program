from .base import BaseCommand
from .context import Context
from models.tournament_manager import TournamentManager


class TournamentListCmd(BaseCommand):

    def __init__(self, club):
        self.club = club

    def execute(self):
        manager = TournamentManager(self.club)

        tournaments = manager.load()

        return Context(
            "tournament-list",
            club=self.club,
            tournaments=tournaments
        )
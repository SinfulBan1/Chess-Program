from .base import BaseCommand
from .context import Context


class CreateFirstRoundCmd(BaseCommand):

    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        self.tournament.create_first_round()
        self.tournament.save()

        return Context(
            "tournament-view",
            tournament=self.tournament
        )
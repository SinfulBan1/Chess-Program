from .base import BaseCommand
from .context import Context

class CompleteRoundCmd(BaseCommand):

    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        current_round = self.tournament.rounds[-1]

        self.tournament.score_round(current_round)

        if not self.tournament.completed:
            self.tournament.create_next_round()

        self.tournament.save()

        return Context(
            "tournament-view",
            tournament=self.tournament
        )
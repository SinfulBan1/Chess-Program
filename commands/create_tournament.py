from commands.context import Context
from models.tournament import Tournament
from .base import BaseCommand

class TournamentCreateCmd(BaseCommand):

    def __init__(self, name, dates, venue, round_num):
        self.name = name
        self.dates = dates
        self.venue = venue
        self.round_num = round_num

    def execute(self):
        tournament = Tournament(
            self.name,
            self.dates,
            self.venue,
            self.round_num
        )
        return Context("tournament-view", tournament=tournament)
from commands.context import Context
from models import TournamentManager
from .base import BaseCommand

class TournamentCreateCmd(BaseCommand):

    def __init__(self, name, start_date, end_date, venue, round_num):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.venue = venue
        self.round_num = round_num

    def execute(self):

        dates = {
            "from": self.start_date,
            "to": self.end_date
        }
    
        tm = TournamentManager()

        tournament = tm.create(
            self.name,
            dates,
            self.venue,
            self.round_num
            )

        return Context("tournament-view", tournament=tournament)
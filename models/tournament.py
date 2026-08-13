from .round import Round
from .player import Player

class Tournament:

    def __init__(self, name, dates, venue, round_num):
        self.name = name
        self.dates = dates
        self.venue = venue
        self.total_round_num = round_num
        self.curr_round_num = 0
        self.completed = False
        self.players = []
        self.rounds = []

    def add_player(self, player):
        if not isinstance(player, Player):
            raise TypeError("Only player objects may be added as players")

        self.players.append(player)

    def add_round(self, tournament_round):
        if not isinstance(tournament_round, Round):
            raise TypeError("Only Round objects can be added as rounds")

        self.rounds.append(tournament_round)
        self.curr_round_num = len(self.rounds)

    def 

    def serialize(self):
        return {
            "name": self.name,
            "dates": self.dates,
            "venue": self.venue,
            "number_of_rounds": self.total_round_num,
            "current_round": self.curr_round_num,
            "completed": self.completed,
            "players": [player.chess_id for player in self.players],
            "rounds": [tournament_round.serialize() for tournament_round in self.rounds]
        }

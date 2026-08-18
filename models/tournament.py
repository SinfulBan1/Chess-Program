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
        self.points = {}
        self.rounds = []

    def add_player(self, player):
        if not isinstance(player, Player):
            raise TypeError("Only player objects may be added as players")
        self.players.append(player)
        self.points[player.chess_id] = 0

    def add_round(self, tournament_round):
        if not isinstance(tournament_round, Round):
            raise TypeError("Only Round objects can be added as rounds")

        self.rounds.append(tournament_round)
        self.curr_round_num = len(self.rounds)
        winners = tournament_round.get_winners()
        drawers = tournament_round.get_draws()
        for winner_id in winners:
            self.update_score(winner_id, 1)
        for drawer_id in drawers:
            self.update_score(drawer_id, 0.5)

    def update_score(self, winner_id, point):
        self.points[winner_id] = self.points.get(winner_id) + point

    def serialize(self):
        return {
            "name": self.name,
            "dates": self.dates,
            "venue": self.venue,
            "number_of_rounds": self.total_round_num,
            "current_round": self.curr_round_num,
            "completed": self.completed,
            "players": [player.chess_id for player in self.players],
            "points": self.points,
            "rounds": [tournament_round.serialize() for tournament_round in self.rounds]
        }

    @classmethod
    def from_data(cls, data, players):
        tournament = cls(
            data["name"],
            data["dates"],
            data["venue"],
            data["number_of_rounds"]
        )

        tournament.curr_round_num = data["current_round"]
        tournament.completed = data["completed"]

        for player_id in data["players"]:
            tournament.add_player(players[player_id])

        for round_data in data["rounds"]:
            tournament.add_round(Round.from_data(round_data, players))

        return tournament
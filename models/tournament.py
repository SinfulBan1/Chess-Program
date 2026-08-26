import random
import json

from .match import Match
from .round import Round
from .player import Player


class Tournament:

    def __init__(self, name, dates, venue, round_num, filepath=None):
        self.name = name
        self.dates = dates
        self.venue = venue
        self.total_round_num = round_num
        self.curr_round_num = 0
        self.filepath = filepath
        self.completed = False
        self.players = []
        self.points = {}
        self.rounds = []

    def save(self):
        if self.filepath is None:
            raise ValueError("Tournament doesn't have a filepath set.")

        with open(self.filepath, "w") as file:
            json.dump(self.serialize(), file, indent=4)

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

    def score_round(self, tournament_round):
        if tournament_round.scored:
            raise ValueError("This round has already been scored.")
        for match in tournament_round.matches:
            if not match.completed:
                raise ValueError("All matches in the round must be completed before scoring.")
        winners = tournament_round.get_winners()
        drawers = tournament_round.get_draws()

        for player_id in winners:
            self.update_score(player_id, 1)

        for player_id in drawers:
            self.update_score(player_id, 0.5)

        if self.curr_round_num == self.total_round_num:
            self.completed = True

        tournament_round.scored = True

    def update_score(self, winner_id, point):
        self.points[winner_id] = self.points.get(winner_id) + point

    def get_standings(self):
        return sorted(
            self.players,
            key=lambda player: self.points[player.chess_id],
            reverse=True
        )

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

    # matchmaking
    def create_first_round(self):
        if self.curr_round_num != 0:
            print("First round already created.")
            return

        if len(self.players) % 2 != 0:
            print("An even number of players is required to start the tournament.")
            return

        if len(self.players) < 2:
            print("There must be at least two players to start a tournament.")
            return

        shuffled_players = self.players.copy()
        random.shuffle(shuffled_players)

        tournament_round = Round()

        for i in range(0, len(shuffled_players), 2):
            player1 = shuffled_players[i]
            player2 = shuffled_players[i+1]

            match = Match(player1, player2)
            tournament_round.add_match(match)

        self.add_round(tournament_round)

    def have_played(self, player1, player2):
        for tournament_round in self.rounds:
            for match in tournament_round.matches:
                if player1 in match.players and player2 in match.players:
                    return True

        return False

    def create_next_round(self):
        if self.curr_round_num == 0:
            raise ValueError("First round must be created first")

        if self.curr_round_num >= self.total_round_num:
            raise ValueError("All rounds already created")

        current_round = self.rounds[-1]

        for match in current_round.matches:
            if not match.completed:
                raise ValueError("All matches in the current round must be completed to make the next round")

        sorted_players = sorted(
            self.players,
            key=lambda player: self.points[player.chess_id],
            reverse=True
        )

        tournament_round = Round()

        while sorted_players:
            player1 = sorted_players.pop(0)

            opponent_index = None
            for i, player2 in enumerate(sorted_players):
                if not self.have_played(player1, player2):
                    opponent_index = i
                    break

            if opponent_index is None:
                opponent_index = 0

            player2 = sorted_players.pop(opponent_index)

            match = Match(player1, player2)
            tournament_round.add_match(match)

        self.add_round(tournament_round)

    @classmethod
    def from_data(cls, data, players, filepath=None):
        tournament = cls(
            data["name"],
            data["dates"],
            data["venue"],
            data["number_of_rounds"],
            filepath
        )

        tournament.completed = data["completed"]

        for player_id in data["players"]:
            tournament.add_player(players[player_id])

        tournament.points = data["points"]

        for round_data in data["rounds"]:
            tournament.add_round(Round.from_data(round_data, players))

        tournament.curr_round_num = data["current_round"]

        return tournament

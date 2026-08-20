from pathlib import Path
import json

from .tournament import Tournament


class TournamentManager:

    def __init__(self, club):
        self.club = club
        self.tournament_dir = Path("data/tournaments")

    def get_players(self):
        return{
            player.chess_id: self.get_player
            for player in self.club.players
        }

    def load(self):
        tournaments = []
        players = self.get_players()

        for tournament_file in self.tournament_dir.glob("*.json"):
            with open(tournament_file, "r") as file:
                data = json.load(file)

            tournament = Tournament.from_data(data, players)
            tournaments.append(tournament)
from pathlib import Path
import json

from .tournament import Tournament
from .club_manager import ClubManager

class TournamentManager:

    def __init__(self):
        self.tournament_dir = Path("data/tournaments")

    def get_players(self):
        players = {}

        club_manager = ClubManager()

        for club in club_manager.clubs:
            for player in club.players:
                players[player.chess_id] = player

        return players

    def load(self):
        tournaments = []
        players = self.get_players()

        for tournament_file in self.tournament_dir.glob("*.json"):
            with open(tournament_file, "r") as file:
                data = json.load(file)

            tournament = Tournament.from_data(data, players)
            tournaments.append(tournament)

        return tournaments
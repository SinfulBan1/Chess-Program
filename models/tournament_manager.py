import json
from pathlib import Path

from .tournament import Tournament
from .club_manager import ClubManager


class TournamentManager:

    def __init__(self, data_folder="data/tournaments"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.tournaments = []

        players = self.get_players()

        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    with open(filepath, "r") as file:
                        data = json.load(file)

                    tournament = Tournament.from_data(data, players)
                    self.tournaments.append(tournament)

                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")

    def get_players(self):
        players = {}

        club_manager = ClubManager()

        for club in club_manager.clubs:
            for player in club.players:
                players[player.chess_id] = player

        return players
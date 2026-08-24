from ..base_screen import BaseScreen
from commands import NoopCmd


class TournamentStandings(BaseScreen):
    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print(f"Tournament: {self.tournament.name}")
        print("Standings:")
        for idx, player in enumerate(self.tournament.get_standings(), 1):
            print(f"{idx}. {player.name}: {self.tournament.points[player.chess_id]}")

    def get_command(self):
        print("B - Back to tournament view")

        value = self.input_string()

        if value.upper() == "B":
            return NoopCmd(
                "tournament-view",
                tournament=self.tournament
            )

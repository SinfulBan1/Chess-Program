from commands import NoopCmd, ExitCmd
from models import ClubManager

from ..base_screen import BaseScreen


class TournamentList(BaseScreen):
    """Screen displaying the tournaments for a club"""

    def __init__(self, tournaments=None):
        self.tournaments = tournaments if tournaments is not None else []

    def display(self):
        print("## Tournaments")

        for idx, tournament in enumerate(self.tournaments, 1):
            print(idx, tournament.name)

    def get_command(self):
        while True:
            print("Select a tournament to view.")
            print("Type 'C' to create a tournament.")
            print("Type 'S' to view clubs.")
            print("Type 'X' to exit.")

            value = self.input_string()

            if value.upper() == "S":
                cm = ClubManager()

                return NoopCmd(
                    "club-list",
                    clubs=cm.clubs
                )

            elif value.upper() == "C":
                return NoopCmd(
                    "tournament-create"
                )

            elif value.upper() == "X":
                return ExitCmd()

            elif value.isdigit():
                value = int(value)

                if value in range(1, len(self.tournaments) + 1):
                    return NoopCmd(
                        "tournament-view",
                        tournament=self.tournaments[value - 1]
                    )

from commands import ClubListCmd, NoopCmd

from ..base_screen import BaseScreen


class TournamentList(BaseScreen):
    """Screen displaying the tournaments for a club"""

    def __init__(self, club, tournaments=None):
        self.club = club
        self.tournaments = tournaments if tournaments is not None else []

    def display(self):
        print("## Tournaments for", self.club.name)

        for idx, tournament in enumerate(self.tournaments, 1):
            print(idx, tournament.name)

    def get_command(self):
        while True:
            print("Select a tournament to view.")
            print("Type 'C' to create a tournament.")
            print("Type 'B' to go back to the club.")

            value = self.input_string()

            if value.upper() == "B":
                return NoopCmd(
                    "club-view",
                    club=self.club
                )

            elif value.upper() == "C":
                return NoopCmd(
                    "tournament-create",
                    club=self.club
                )

            elif value.isdigit():
                value = int(value)

                if value in range(1, len(self.tournaments) + 1):
                    return NoopCmd(
                        "tournament-view",
                        club=self.club,
                        tournament=self.tournaments[value - 1]
                    )
from commands import TournamentListCmd, NoopCmd

from models import tournament

from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    """Screen displayed when viewing a tournament"""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("##", self.tournament.name)

        print("Venue:", self.tournament.venue)

        print(
            "Dates:",
            self.tournament.dates["from"],
            "to",
            self.tournament.dates["to"]
        )

        print(
            "Rounds:",
            f"{self.tournament.curr_round_num}/{self.tournament.total_round_num}"
        )

        print("Players:", len(self.tournament.players))

        if self.tournament.completed:
            print("Status: Completed")
        else:
            print("Status: In Progress")

    def get_command(self):
        while True:
            print("\nWhat would you like to do?")
            print("A - Add players")
            print("S - View standings")
            print("F - Create first round")
            print("N - Create next round")
            print("B - Back")

            value = self.input_string()

            if value.upper() == "B":
                return TournamentListCmd()
            elif value.upper() == "A":
                if tournament.curr_round != 0:
                    raise ValueError("Tournament Already Started")
                else:
                    return NoopCmd(
                        "player-select",
                        added_players=self.tournament.players,
                        tournament=self.tournament
                    )
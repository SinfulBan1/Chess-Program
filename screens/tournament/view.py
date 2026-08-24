from commands import TournamentListCmd, NoopCmd, CreateFirstRoundCmd

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

        if self.tournament.rounds:
            print("Current Matches:")
            curr_round = self.tournament.rounds[-1]
            for idx, match in enumerate(curr_round.matches, 1):
                print(f"{idx}. {match.players[0]} vs {match.players[1]}")

    def get_command(self):
        while True:
            print("\nWhat would you like to do?")
            print("A - Add players")
            print("S - View standings")
            print("F - Create first round")
            print("N - Select winners and create next round")
            print("G - Generate Report")
            print("B - Back")

            value = self.input_string()

            if value.upper() == "B":
                return TournamentListCmd()
            elif value.upper() == "A":
                if self.tournament.curr_round_num != 0:
                    print("The tournament already started. Cannot add new players")
                else:
                    return NoopCmd(
                        "player-select",
                        added_players=self.tournament.players,
                        tournament=self.tournament
                    )
            elif value.upper() == "F":
                return CreateFirstRoundCmd(self.tournament)
            elif value.upper() == "N":
                if self.tournament.curr_round_num == 0:
                    print("The tournament has not started yet.")
                elif self.tournament.completed:
                    print("The tournament is already completed.")
                else:
                    print("Are you sure you want to advance to the next round? Y/N")
                    confirmation_value = self.input_string()

                    if confirmation_value.upper() == "Y":
                        return NoopCmd(
                            "round-results",
                            tournament=self.tournament
                        )
                    elif confirmation_value.upper() == "N":
                        return NoopCmd("tournament-view", tournament=self.tournament)
            elif value.upper() == "S":
                return NoopCmd("tournament-standings", tournament=self.tournament)
            elif value.upper() == "G":
                return NoopCmd("tournament-report", tournament=self.tournament)

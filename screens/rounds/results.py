from commands import CompleteRoundCmd

from ..base_screen import BaseScreen


class RoundResults(BaseScreen):
    def __init__(self, tournament):
        self.tournament = tournament
        self.current_round = tournament.rounds[-1]

    def display(self):
        print("## Round Results")
        print("Round:", self.tournament.curr_round_num)

        for idx, match in enumerate(self.current_round.matches, 1):
            player1 = match.players[0]
            player2 = match.players[1]

            print(
                idx,
                player1.name,
                "vs",
                player2.name
            )

    def get_command(self):
        for match in self.current_round.matches:
            player1 = match.players[0]
            player2 = match.players[1]

            while True:
                print()
                print(player1.name, "vs", player2.name)
                print("1 -", player1.name, "wins")
                print("2 -", player2.name, "wins")
                print("D - Draw")

                value = self.input_string()

                if value == "1":
                    match.set_winner(player1)
                    break

                elif value == "2":
                    match.set_winner(player2)
                    break

                elif value.upper() == "D":
                    match.set_draw()
                    break

                else:
                    print("Please enter 1, 2, or D.")

        return CompleteRoundCmd(self.tournament)

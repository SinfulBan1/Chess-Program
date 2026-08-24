from ..base_screen import BaseScreen
from commands import NoopCmd


class TournamentReport(BaseScreen):

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("## Tournament Report")
        print("Tournament:", self.tournament.name)
        print(
            "Dates:",
            self.tournament.dates["from"],
            "to",
            self.tournament.dates["to"]
        )

        print("\nStandings:")

        for idx, player in enumerate(
            self.tournament.get_standings(),
            1
        ):
            points = self.tournament.points[player.chess_id]

            print(
                f"{idx}. {player.name} - {points} points"
            )

        print("\nRounds:")

        for round_idx, tournament_round in enumerate(
            self.tournament.rounds,
            1
        ):
            print(f"\nRound {round_idx}")

            for match_idx, match in enumerate(
                tournament_round.matches,
                1
            ):
                player1 = match.players[0]
                player2 = match.players[1]

                if not match.completed:
                    result = "Not completed"

                elif match.winner is None:
                    result = "Draw"

                else:
                    result = f"{match.winner.name} won"

                print(
                    f"{match_idx}. "
                    f"{player1.name} vs {player2.name} "
                    f"- {result}"
                )

    def get_command(self):
        while True:
            print("\nB - Back to tournament")

            value = self.input_string()

            if value.upper() == "B":
                return NoopCmd(
                    "tournament-view",
                    tournament=self.tournament
                )
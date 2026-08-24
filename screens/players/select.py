from ..base_screen import BaseScreen

from commands import NoopCmd

from models import TournamentManager


class PlayerSelect(BaseScreen):
    def __init__(self, added_players, tournament):
        self.added_players = added_players
        self.tournament = tournament
        tm = TournamentManager()
        self.players = tm.get_players()
        self.remaining_players = []
        for player in self.players:
            if player not in self.added_players:
                self.remaining_players.append(player)
            

    def display(self):
        print("## Players Available")

        for idx, player in enumerate(self.remaining_players, 1):
            print(idx, player.name, player.chess_id)

    def get_command(self):
        while True:
            print("Select a player to add to the tournament.")
            print("B - Back to tournament")

            value = self.input_string()

            if value.upper() == "B":
                return NoopCmd(
                    "tournament-view",
                    tournament=self.tournament
                )

            elif value.isdigit():
                value = int(value)

                if value in range(1, len(self.remaining_players) + 1):

                    new_player = self.remaining_players[value - 1]

                    self.tournament.add_player(new_player)
                    self.added_players = self.tournament.players
                    self.tournament.save()

                    print("Player added.")

                    return NoopCmd(
                        "player-select",
                        added_players=self.added_players,
                        tournament=self.tournament
                    )

                else:
                    print("Must select a valid player index.")
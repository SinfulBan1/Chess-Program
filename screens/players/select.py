from ..base_screen import BaseScreen

from commands import NoopCmd

from models import TournamentManager


class PlayerSelect(BaseScreen):
    def __init__(self, added_players, tournament, matches=None):
        self.added_players = added_players
        self.tournament = tournament
        tm = TournamentManager()
        self.players = list(tm.get_players().values())
        self.remaining_players = []
        for player in self.players:
            if player not in self.added_players:
                self.remaining_players.append(player)
        if matches is not None:
            self.remaining_players = matches

    def display(self):
        print("## Players Available")

        for idx, player in enumerate(self.remaining_players, 1):
            print(idx, player.name, player.chess_id)

    def get_command(self):
        while True:
            print("Select a player to add to the tournament.")
            print("S - Search players")
            print("R - Reset Search Filter")
            print("B - Back to tournament")

            value = self.input_string()

            if value.upper() == "B":
                return NoopCmd(
                    "tournament-view",
                    tournament=self.tournament
                )
            elif value.upper() == "S":
                search_value = self.input_string(
                    prompt="Enter Chess ID or part of the player's name"
                ).lower()

                matches = []

                for player in self.remaining_players:
                    if (
                        search_value in player.name.lower()
                        or search_value == player.chess_id.lower()
                    ):
                        matches.append(player)

                return NoopCmd(
                    "player-select",
                    added_players=self.added_players,
                    tournament=self.tournament,
                    matches=matches
                )
            elif value.upper() == "R":
                return NoopCmd(
                    "player-select",
                    added_players=self.added_players,
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

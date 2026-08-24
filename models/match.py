# matches class


class Match:
    # hold 2 players
    # track if match is complete
    # track winner
    # update player tournament points
    # use with JSON

    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.completed = False
        self.winner = None

    def set_winner(self, winner):
        if winner not in self.players:  # if the winner isn't input correctly
            raise ValueError("Winner must be one of the players in the match.")

        self.winner = winner
        self.completed = True

    def set_draw(self):
        self.winner = None  # adding this in case someone accidentally sets winner first then realizes it was a draw
        self.completed = True

    def serialize(self):
        data = {
            "players": [player.chess_id for player in self.players],
            "completed": self.completed,
            "winner": self.winner.chess_id if self.winner else None
        }
        return data

    @classmethod
    def from_data(cls, data, players):
        player1 = players[data["players"][0]]
        player2 = players[data["players"][1]]

        match = cls(player1, player2)

        match.completed = data["completed"]

        if data["winner"] is not None:
            match.winner = players[data["winner"]]

        return match

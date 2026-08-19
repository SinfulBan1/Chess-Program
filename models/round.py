from .match import Match

class Round:
    def __init__(self, matches=None):
        self.matches = matches if matches is not None else []

    def add_match(self, match):
        if not isinstance(match, Match):
            raise TypeError("Round can only contain Matches. Attempted match addition was not Match object")

        self.matches.append(match)

    def get_winners(self):
        winners = []
        for match in self.matches:
            if match.winner is not None:
                winners.append(match.winner.chess_id)
        return winners

    def get_draws(self):
        drawers = []
        for match in self.matches:
            if match.completed and match.winner is None:
                for drawer_id in match.players:
                    drawers.append(drawer_id.chess_id)

        return drawers

    def serialize(self):
        return [match.serialize() for match in self.matches]

    @classmethod
    def from_data(cls, data, players):
        round_obj = cls()

        for match_data in data:
            match = Match.from_data(match_data, players)
            round_obj.add_match(match)

        return round_obj
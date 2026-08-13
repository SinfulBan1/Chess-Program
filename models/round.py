from .match import Match

class Round:
    def __init__(self, matches=None):
        self.matches = matches if matches is not None else []

    def add_match(self, match):
        if not isinstance(match, Match):
            raise TypeError("Round can only contain Matches. Attempted match addition was not Match object")

        self.matches.append(match)

    def serialize(self):
        return [match.serialize() for match in self.matches]
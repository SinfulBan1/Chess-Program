# matches class
from models.player import Player

class Match:
    # hold 2 players
    # track if match is complete
    # track winner
    # update player tournament points
    # use with JSON - need to implement


    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.completed = False
        self.winner = None

    def set_winner(self, winner):
        if winner not in self.players: # if the winner isn't input correctly
            raise ValueError("Winner must be one of the players in the match.")

        self.winner = winner
        self.completed = True

    def set_draw(self):
        self.winner = None # adding this in case someone accidentally sets winner first then realizes it was a draw
        self.completed = True

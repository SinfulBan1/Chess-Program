from models.match import Match
from models.player import Player

player1 = Player(
    "Alice",
    "alice@example.com",
    "AB12345",
    "01-01-2000"
)

player2 = Player(
    "Bob",
    "bob@example.com",
    "CD67890",
    "01-01-2000"
)

player3 = Player(
    "Joe",
    "joe@example.com",
    "WD44321",
    "01-02-2000"
)

match = Match(player1, player2)

print(match.players)
print(match.completed)
print(match.winner)

match.set_draw()

print(match.completed)
print(match.winner)

# match.set_winner(player3)

match.set_winner(player1)

print(match.completed)
print(match.winner)

print(match.serialize())
from models.match import Match
from models.player import Player
from models.round import Round

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
    "Charlie",
    "charlie@example.com",
    "EF11111",
    "01-01-2000"
)

player4 = Player(
    "Dave",
    "dave@example.com",
    "GH22222",
    "01-01-2000"
)


match1 = Match(player1, player2)
match2 = Match(player3, player4)

match1.set_draw()
match2.set_winner(player3)

round1 = Round()

round1.add_match(match1)
round1.add_match(match2)

print(round1.matches)
print(round1.serialize())


round_data = [
    {
        "players": ["AB12345", "CD67890"],
        "completed": True,
        "winner": "AB12345"
    },
    {
        "players": ["EF11111", "GH22222"],
        "completed": True,
        "winner": None
    }
]

players = {
    player1.chess_id: player1,
    player2.chess_id: player2,
    player3.chess_id: player3,
    player4.chess_id: player4
}

loaded_round = Round.from_data(round_data, players)

print(loaded_round.matches)
print(loaded_round.matches[0].winner.name)
print(loaded_round.matches[1].winner)
print(loaded_round.serialize())
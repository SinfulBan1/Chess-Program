from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament


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


tournament = Tournament(
    "Test Tournament",
    {
        "from": "01-08-2026",
        "to": "10-08-2026"
    },
    "Test Venue",
    4
)


tournament.add_player(player1)
tournament.add_player(player2)
tournament.add_player(player3)
tournament.add_player(player4)


match1 = Match(player1, player2)
match2 = Match(player3, player4)

match1.set_winner(player1)
match2.set_draw()


round1 = Round()

round1.add_match(match1)
round1.add_match(match2)


tournament.add_round(round1)

print(tournament.serialize())
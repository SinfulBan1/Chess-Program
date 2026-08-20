from models.tournament_manager import TournamentManager

tm = TournamentManager()

tournament = tm.create(
    "Test Tournament",
    {
        "from": "2026-08-20",
        "to": "2026-08-21"
    },
    "Test Venue",
    4
)

print(tournament.name)
print(tournament.filepath)
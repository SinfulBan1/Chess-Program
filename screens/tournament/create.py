from commands import TournamentCreateCmd

from ..base_screen import BaseScreen


class TournamentCreate(BaseScreen):
    """Screen displayed when creating a tournament"""

    def get_command(self):
        attrs = [
            ("name", "Tournament name", self.input_string),
            ("start_date", "Start date", self.input_date),
            ("end_date", "End date", self.input_date),
            ("venue", "Venue", self.input_string)
        ]

        data = {}

        for key, prompt, func in attrs:
            data[key] = func(prompt=prompt)
            
        data["round_num"] = self.input_int(
            prompt="Number of rounds",
            minimum=1
        )

        return TournamentCreateCmd(**data)
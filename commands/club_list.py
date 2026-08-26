from commands.context import Context
from .base import BaseCommand


class ClubListCmd(BaseCommand):
    """Command to get the list of clubs"""

    def execute(self):
        return Context("tournament-list")

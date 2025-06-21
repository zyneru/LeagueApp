# match_loader.py
"""
match_loader.py

This module provides the MatchLoader class, which reads and parses lines of text-based
match results, constructs Team and Match objects, and maintains a list of parsed matches.

Dependencies:
    - Team (models.team): Represents an individual team.
    - Match (models.match): Represents a match between two teams with their scores.
    - TextSplitter (functions.text_splitter): Parses match result lines into team names and scores.

Each input line should be formatted as:
    "Team Alpha 3, Team Beta 2"

Example:
    loader = MatchLoader(lines)
    print(loader.get_summary())
"""

from models.team import Team
from models.match import Match
from functions.text_splitter import TextSplitter

class MatchLoader:
    """
    Loads matches from a list of text lines, creating corresponding Team and Match objects.

    Attributes:
        teams (dict): A dictionary mapping team names to Team instances.
        matches (list): A list of Match instances created from the input lines.

    Methods:
        get_summary() -> str:
            Returns a newline-separated string summarizing all matches.
    """

    def __init__(self, lines: list[str]):
        """
        Initializes the MatchLoader by parsing lines into teams and matches.

        Args:
            lines (list[str]): A list of strings, each representing a match result in the format:
                               "Team Name A <scoreA>, Team Name B <scoreB>"

        Behavior:
            - If a team is mentioned that hasn't been seen before, a new Team instance is created.
            - A Match instance is created for each line and added to the matches list.
        """

        self.teams = {}
        self.matches = []

        for line in lines:
            self._parse_input(line)

    def get_summary(self):
        """
        Returns:
            str: A newline-separated string representing the matches.
        """
        return "\n".join(match.get_summary() for match in self.matches)

    def _parse_input(self, text: str):
        split_text = TextSplitter(text)

        if self.teams.get(split_text.team_name1) is None:
            self.teams[split_text.team_name1] = Team(split_text.team_name1)

        if self.teams.get(split_text.team_name2) is None:
            self.teams[split_text.team_name2] = Team(split_text.team_name2)

        self.matches.append(
            Match(
                self.teams[split_text.team_name1],
                split_text.score1,
                self.teams[split_text.team_name2],
                split_text.score2
            )
        )

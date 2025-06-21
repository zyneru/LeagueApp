# text_splitter.py
"""
text_splitter.py

This module provides the `TextSplitter` class for parsing structured game result strings
into team names and corresponding scores.
"""

class TextSplitter:
    """
    A utility class for parsing a game result string into team names and scores.

    The input string is expected to follow the format:
    `"Team Name A <scoreA>, Team Name B <scoreB>"`

    Attributes:
        team_name1 (str): The name of the first team.
        team_name2 (str): The name of the second team.
        score1 (int): The score of the first team.
        score2 (int): The score of the second team.
    """

    def __init__(self, text: str):
        """
        Parses a match result string into two team names and their respective scores.

        The input string should contain exactly two team results separated by a comma.
        Each team result consists of the team name followed by its score as an integer.
        For example: "Team Alpha 3, Team Beta 2"

        Args:
            text (str): The input string containing two teams and their scores.

        Raises:
            ValueError: If the input format is invalid, scores are not integers,
                        or team names are missing.
        """

        parts = [part.strip() for part in text.strip().split(",")]
        if len(parts) != 2:
            raise ValueError("Input must contain two team results separated by a single comma.")

        self.team_name1, self.score1 = self._parse_team_result(parts[0])
        self.team_name2, self.score2 = self._parse_team_result(parts[1])

    def _parse_team_result(self, team_result: str):
        """
        Parses a single team result string into a team name and score.

        Args:
            team_result (str): A string containing a team name and a score.

        Returns:
            tuple: (team_name (str), score (int))

        Raises:
            ValueError: If the team result does not contain at least a name and score,
                        or if the score is not a valid integer.
        """
        components = team_result.split()
        if len(components) < 2:
            raise ValueError("Each match result must include at least a name and a score.")
        try:
            score = int(components[-1])
        except ValueError as exc:
            raise ValueError(f"Score '{components[-1]}' is not a valid integer.") from exc
        team_name = " ".join(components[:-1]).strip()
        if not team_name:
            raise ValueError("Team name cannot be empty.")
        return team_name, score

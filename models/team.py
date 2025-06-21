# team.py
"""
team.py

This module defines the Team class, which represents a sports team within a league.

Each team tracks:
- Its name
- Accumulated points
- Number of matches played
- Current league rank

Used by other components like Match, MatchLoader, and LeagueProcessor to manage and
display team statistics.
"""

class Team:
    """
    Represents a team in a league and tracks performance statistics.

    Attributes:
        team_name (str): The name of the team.
        points (int): Total league points accumulated by the team.
        match_count (int): Number of matches the team has played.
        league_rank (int): Current rank in the league (set externally).
    
    Methods:
        add_result(points: int):
            Adds points from a match and increments the match count.

        set_league_rank(league_rank: int):
            Sets the team's current rank in the league table.

        get_summary() -> str:
            Returns a formatted summary string of the team's stats.
    """

    def __init__(self, team_name):
        """
        Initializes a Team instance with the given team name.

        Args:
            team_name (str): The name of the team.
        """

        self.points = 0
        self.match_count = 0
        self.team_name = team_name
        self.league_rank = 99

    def add_result(self, points: int):
        """
        Updates the team's stats with points from a completed match.

        Args:
            points (int): Points earned in a match (typically 0, 1, or 3).
        """

        self.points += points
        self.match_count += 1

    def set_league_rank(self, league_rank: int):
        """
        Sets the team's league rank.

        Args:
            league_rank (int): The team's rank position in the league table.
        """
        self.league_rank = league_rank

    def get_summary(self):
        """
        Returns:
            str: A formatted summary line showing the team's rank, name, points, and matches played.
        """
        matches_word = "match" if self.match_count == 1 else "matches"
        return (
            f"{self.league_rank}."
            f" {self.team_name},"
            f" {self.points} pts,"
            f" {self.match_count} {matches_word}"
        )

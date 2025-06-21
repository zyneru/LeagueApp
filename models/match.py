# match.py
"""
match.py

This module defines the Match class, which represents a single match between two teams.
It calculates match outcomes (win/loss/draw), assigns points accordingly, and provides
a human-readable summary of the match.

Dependencies:
    - MatchResult (models.match_result): Enum for match outcomes (DRAW, WINNER_TEAM1, WINNER_TEAM2).
    - Team (models.team): Represents a team and stores its accumulated results.

Example:
    match = Match(team_a, 2, team_b, 2)
    print(match.get_summary())
"""

from models.match_result import MatchResult
from models.team import Team

class Match:
    """
    Represents a match between two teams, calculates the result, and assigns league points.

    Attributes:
        team1 (Team): The first team.
        score1 (int): Score of the first team.
        team2 (Team): The second team.
        score2 (int): Score of the second team.
        points1 (int): League points earned by team1.
        points2 (int): League points earned by team2.
        match_result (MatchResult): Enum value representing the result of the match.

    Methods:
        calculate_points():
            Determines the outcome of the match and assigns points based on scores.

        assign_points():
            Adds the match points to each team's record.

        get_summary() -> str:
            Returns a human-readable summary of the match and outcome.
    """

    def __init__(self, team1: Team, score1: int, team2: Team, score2: int):
        """
        Initializes a Match instance with two teams and their scores.

        Args:
            team1 (Team): The first team.
            score1 (int): Score for team1.
            team2 (Team): The second team.
            score2 (int): Score for team2.

        Side Effects:
            - Determines the result and point allocation.
            - Updates each team's points via their add_result method.
        """

        self.match_result = MatchResult.DRAW
        self.team1 = team1
        self.score1 = score1
        self.team2 = team2
        self.score2 = score2
        self._calculate_points()
        self._assign_points()

    def get_summary(self):
        """
        Returns:
            str: A string summarizing the match result, including scores, points, and outcome.
        """
        return (
            f"Match: {self.team1.team_name} {self.score1} ({self.points1} pts) vs "
            f"{self.team2.team_name} {self.score2} ({self.points2} pts) - {self.match_result.name}"
        )

    def _calculate_points(self):
        """
        Determines the match result based on scores and sets the corresponding points
        and result status (draw, win, or loss).
        """

        if self.score1 == self.score2:
            self.points1 = 1
            self.points2 = 1
            self.match_result = MatchResult.DRAW
            return

        if self.score1 > self.score2:
            self.points1 = 3
            self.points2 = 0
            self.match_result = MatchResult.WINNER_TEAM1
            return

        if self.score2 > self.score1:
            self.points1 = 0
            self.points2 = 3
            self.match_result = MatchResult.WINNER_TEAM2
            return

    def _assign_points(self):
        """
        Applies the calculated points to each team via their add_result method.
        """
        self.team1.add_result(self.points1)
        self.team2.add_result(self.points2)

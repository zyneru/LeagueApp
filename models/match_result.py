# match_result.py
"""
match_result.py

Defines the MatchResult enumeration used to represent possible outcomes of a match.

The enum values distinguish between a draw and which team won.
"""

from enum import Enum

class MatchResult(Enum):
    """
    Enumeration of possible match outcomes.

    Members:
        DRAW: Indicates the match ended in a draw.
        WINNER_TEAM1: Indicates the first team won the match.
        WINNER_TEAM2: Indicates the second team won the match.
    """

    DRAW = 1
    WINNER_TEAM1 = 2
    WINNER_TEAM2 = 3

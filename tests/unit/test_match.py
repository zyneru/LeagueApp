from models.team import Team
from models.match import Match
from models.match_result import MatchResult

def test_team1_wins():
    team1 = Team("Team A")
    team2 = Team("Team B")
    match = Match(team1, 2, team2, 1)

    assert match.points1 == 3
    assert match.points2 == 0
    assert match.match_result == MatchResult.WINNER_TEAM1
    assert team1.points == 3
    assert team2.points == 0

def test_team2_wins():
    team1 = Team("Team A")
    team2 = Team("Team B")
    match = Match(team1, 0, team2, 2)

    assert match.points1 == 0
    assert match.points2 == 3
    assert match.match_result == MatchResult.WINNER_TEAM2

def test_draw():
    team1 = Team("Team A")
    team2 = Team("Team B")
    match = Match(team1, 1, team2, 1)

    assert match.points1 == 1
    assert match.points2 == 1
    assert match.match_result == MatchResult.DRAW

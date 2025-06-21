from models.team import Team
from functions.league_processor import LeagueProcessor

def test_league_ranking_with_unique_points():
    team1 = Team("Alpha")
    team2 = Team("Beta")
    team3 = Team("Gamma")

    team1.add_result(3)
    team2.add_result(1)
    team3.add_result(2)

    LeagueProcessor([team1, team2, team3])

    assert team1.league_rank == 1
    assert team3.league_rank == 2
    assert team2.league_rank == 3

def test_league_ranking_with_tied_points():
    team1 = Team("Alpha")
    team2 = Team("Beta")

    team1.add_result(3)
    team2.add_result(3)

    LeagueProcessor([team1, team2])

    assert team1.league_rank == 1
    assert team2.league_rank == 1

def test_summary_output():
    team = Team("Delta")
    team.add_result(2)
    team.set_league_rank(1)
    processor = LeagueProcessor([team])
    output = processor.get_league_results()
    assert "1. Delta" in output
    assert "2 pts" in output

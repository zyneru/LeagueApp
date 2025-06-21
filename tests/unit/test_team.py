from models.team import Team


def test_add_result_and_summary():
    team = Team("Team Test1")
    team.add_result(3)
    team.add_result(1)
    team.set_league_rank(1)
    summary = team.get_summary()
    
    assert team.points == 4
    assert team.match_count == 2
    assert "Team Test1" in summary
    assert "4 pts" in summary
    assert "2 matches" in summary

def test_match_count_wording():
    team = Team("Solo Team")
    team.add_result(1)
    team.set_league_rank(2)
    summary = team.get_summary()
    assert "1 match" in summary

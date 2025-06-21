from functions.match_loader import MatchLoader


def test_loading_matches_and_teams():
    lines = [
        "Team A 2, Team B 1",
        "Team A 1, Team C 1",
        "Team B 3, Team C 0"
    ]
    loader = MatchLoader(lines)

    assert len(loader.matches) == 3
    assert len(loader.teams) == 3
    assert "Team A" in loader.teams
    assert "Team B" in loader.teams
    assert "Team C" in loader.teams

def test_summary_format():
    lines = ["Team X 4, Team Y 2"]
    loader = MatchLoader(lines)
    summary = loader.get_summary()

    assert "Match: Team X" in summary
    assert "Team Y" in summary
    assert "pts" in summary

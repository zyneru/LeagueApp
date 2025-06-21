import pytest
from functions.text_splitter import TextSplitter

def test_valid_input():
    splitter = TextSplitter("Team Alpha 2, Team Beta 3")
    assert splitter.team_name1 == "Team Alpha"
    assert splitter.score1 == 2
    assert splitter.team_name2 == "Team Beta"
    assert splitter.score2 == 3

def test_invalid_format_missing_comma():
    with pytest.raises(
        ValueError,
        match="Input must contain two team results separated by a single comma."
    ):
        TextSplitter("Team Alpha 2 Team Beta 3")

def test_invalid_format_missing_score():
    with pytest.raises(
        ValueError,
        match="Each match result must include at least a name and a score."
    ):
        TextSplitter("Team, Team Beta 3")

def test_invalid_score():
    with pytest.raises(
        ValueError,
        match="Score 'X' is not a valid integer."
    ):
        TextSplitter("Team Alpha X, Team Beta 3")

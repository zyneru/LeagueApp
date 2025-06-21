import pytest
from io import StringIO
from league_calculator import main

@pytest.fixture
def sample_matches():
    return [
        "Team A 2, Team B 1",
        "Team C 0, Team A 3",
        "Team B 1, Team C 1"
    ]

def test_integration_raw_text_input(capsys, sample_matches):
    raw_text = "\\n".join(sample_matches)

    class Args:
        file = None
        text = raw_text

    main(Args)
    captured = capsys.readouterr()

    assert "Input values (from raw text):" in captured.out
    assert "Matches:" in captured.out
    assert "League results:" in captured.out
    assert "Team A" in captured.out
    assert "Team B" in captured.out
    assert "Team C" in captured.out
    assert "Team A" in captured.out and "6 pts" in captured.out

def test_integration_file_input(monkeypatch, capsys, sample_matches):
    fake_file_content = "\n".join(sample_matches)
    filename = "fakefile.txt"

    def mock_open(*args, **kwargs):
        if args[0] == filename:
            return StringIO(fake_file_content)
        raise FileNotFoundError()

    monkeypatch.setattr("builtins.open", mock_open)

    class Args:
        file = filename
        text = None

    main(Args)
    captured = capsys.readouterr()

    assert "Input values (from file):" in captured.out
    assert "Matches:" in captured.out
    assert "League results:" in captured.out

def test_integration_invalid_format_exit(capsys):
    bad_input = ["Team A 2 Team B 3"]

    class Args:
        file = None
        text = "\\n".join(bad_input)

    with pytest.raises(SystemExit):
        main(Args)

    captured = capsys.readouterr()
    assert "Scores must be valid integers" not in captured.out

def test_integration_missing_file_exit(capsys):
    class Args:
        file = "missing.txt"
        text = None

    with pytest.raises(SystemExit):
        main(Args)

    captured = capsys.readouterr()
    assert "was not found" in captured.out

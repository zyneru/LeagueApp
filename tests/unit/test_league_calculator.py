import pytest
from io import StringIO
from league_calculator import calculate_league, parse_args, main

def test_run_league_calculator(capsys):
    test_lines = [
        "Team A 2, Team B 1",
        "Team C 0, Team A 3",
        "Team B 1, Team C 1"
    ]

    calculate_league(test_lines)
    captured = capsys.readouterr()

    assert "Matches:" in captured.out
    assert "Team A" in captured.out
    assert "League results:" in captured.out


def test_parse_args_no_args():
    args = parse_args([])
    assert args.file is None
    assert args.text is None

def test_parse_args_with_file():
    args = parse_args(['--file', 'test.txt'])
    assert args.file == 'test.txt'
    assert args.text is None

def test_parse_args_with_text():
    raw_text = "Team A 1, Team B 2\\nTeam C 3, Team D 1"
    args = parse_args(['--text', raw_text])
    assert args.text == raw_text
    assert args.file is None

def test_parse_args_invalid_arg():
    with pytest.raises(SystemExit):
        parse_args(['--unknown'])

def test_main_file_input(monkeypatch, capsys):
    fake_file_content = "Team A 1, Team B 2\nTeam C 3, Team D 1\n"
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

def test_main_text_input(capsys):
    raw_text = "Team A 1, Team B 2\\nTeam C 3, Team D 1"

    class Args:
        file = None
        text = raw_text

    main(Args)
    captured = capsys.readouterr()
    assert "Input values (from raw text):" in captured.out
    assert "Matches:" in captured.out
    assert "League results:" in captured.out

def test_main_both_args_exit(capsys):
    class Args:
        file = "file.txt"
        text = "some text"

    with pytest.raises(SystemExit):
        main(Args)
    captured = capsys.readouterr()
    assert "Please provide either --file or --text, not both." in captured.out

def test_main_no_args_exit(capsys):
    class Args:
        file = None
        text = None

    with pytest.raises(SystemExit):
        main(Args)
    captured = capsys.readouterr()
    assert "No input provided" in captured.out

def test_main_file_not_found(monkeypatch, capsys):
    filename = "nonexistent.txt"

    def mock_open(*args, **kwargs):
        raise FileNotFoundError()

    monkeypatch.setattr("builtins.open", mock_open)

    class Args:
        file = filename
        text = None

    with pytest.raises(SystemExit):
        main(Args)
    captured = capsys.readouterr()
    assert f"Error: The file '{filename}' was not found." in captured.out

# ⚽ League Calculator

A command-line tool to process football match results, calculate league standings, and display rankings.

---

## 📝 Features

- Accepts input from a file (`--file`) or raw text via command line (`--text`)
- Parses match results and calculates league points
- Outputs match summaries and final league rankings
- Includes unit and integration tests
- Supports test coverage with `pytest` and `pytest-cov`

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/zyneru/LeagueApp.git
cd league-calculator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Using a file:

```bash
python league_calculator.py --file matches.txt
```

### Using raw text:

```bash
python league_calculator.py --text "Team A 1, Team B 2\nTeam C 3, Team D 1"
```

## Input format

Each match must be formatted as:

```
Team X <score>, Team Y <score>
```

Examples:

```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
```

Multiline input via --text should use literal \n separators.

## Running tests

### Run all tests:

```bash
pytest
```

### Run with coverage:

```bash
pytest --cov=.
```

You can also target specific test types:

```bash
pytest tests/unit/
pytest tests/integration/
```

## Project Structure

```bash
league_calculator.py      # Main entry point script
functions/                # MatchLoader, LeagueProcessor, TextSplitter, etc.
models/                   # Team, Match, MatchResult classes
tests/
│
├── unit/                 # Unit tests
└── integration/          # Integration tests

```

### Example Output

```bash
======================================================================
Matches:
======================================================================
Match: Team A 2 (3 pts) vs Team B 1 (0 pts) - WINNER_TEAM1
Match: Team C 0 (0 pts) vs Team A 3 (3 pts) - WINNER_TEAM1
Match: Team B 1 (1 pts) vs Team C 1 (1 pts) - DRAW
======================================================================
League results:
======================================================================
1. Team A, 6 pts, 2 matches
2. Team B, 1 pts, 2 matches
2. Team C, 1 pts, 2 matches
======================================================================
```

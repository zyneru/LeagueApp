"""
league_calculator.py

Entry point script to process match data from a file or raw text input,
calculate league standings, and display match and ranking summaries.

This script supports two input modes:
    - --file <filename>: Read match results from a file (one match per line).
    - --text "<raw_input>": Provide raw multiline match input via command line
      (lines separated by literal '\n').

Example usage:
    python league_calculator.py --file matches.txt
    python league_calculator.py --text "Team A 1, Team B 2\nTeam C 3, Team D 1"

Outputs:
    - Raw input (if present)
    - Match summaries
    - Final league standings
"""

import argparse
import sys
from functions.match_loader import MatchLoader
from functions.league_processor import LeagueProcessor

RULE_LINE = "=" * 70

def parse_args(args=None):
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="League Calculator: Process match results and compute league standings.",
        epilog=(
            "Example usage:\n"
            "  python league_calculator.py --file matches.txt\n"
            "  python league_calculator.py --text \"Team A 3, Team B 2\\nTeam C 1, Team D 1\""
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--file",
        type=str,
        help="Path to a text file containing match results.\n"
             "Each line must follow the format: 'Team X <score>, Team Y <score>'"
    )

    parser.add_argument(
        "--text",
        type=str,
        help="Raw match results as a string, separated by '\\n'.\n"
             "Example: \"Team A 3, Team B 2\\nTeam C 1, Team D 1\""
    )

    return parser.parse_args(args)


def print_section(title: str, content: str):
    """
    Prints a formatted section with a title, content, and divider lines.

    Args:
        title (str): The section title or heading.
        content (str): The content to print under the section title.
    """
    print(RULE_LINE)
    print(title)
    print(RULE_LINE)
    print(content)
    print(RULE_LINE)


def calculate_league(lines: list[str]):
    """
    Calculates league standings from input lines and prints the results.

    Args:
        lines (list[str]): List of match result strings.
    """
    match_loader = MatchLoader(lines)
    print_section("Matches:", match_loader.get_summary().strip())
    league_processor = LeagueProcessor(match_loader.teams.values())
    print_section("League results:", league_processor.get_league_results().strip())


def main(args):
    """
    Main function that processes input from file or raw text and runs league calculation.

    Args:
        args (argparse.Namespace): Parsed command line arguments.
    """
    if args.file and args.text:
        print("Please provide either --file or --text, not both.")
        sys.exit(1)

    lines = []

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as file:
                lines = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: The file '{args.file}' was not found.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

        print_section("Input values (from file):", "\n".join(lines))

    elif args.text:
        lines = [line.strip() for line in args.text.split("\\n") if line.strip()]
        print_section("Input values (from raw text):", "\n".join(lines))

    else:
        print("No input provided. Use --file <filename> or --text <raw_text> to specify input.")
        sys.exit(1)

    calculate_league(lines)


if __name__ == "__main__":
    args = parse_args()
    main(args)

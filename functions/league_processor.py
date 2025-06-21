# league_processor.py
"""
league_processor.py

This module defines the LeagueProcessor class, which is responsible for ranking teams
in a sports league based on their accumulated points and generating a formatted summary
of the league standings.

Teams are sorted in descending order by points. In the event of a tie, teams are
ordered alphabetically by name. Teams with equal points share the same rank.

Example Usage:
    processor = LeagueProcessor(teams_dict)
    print(processor.get_league_results())
"""

from models.team import Team

class LeagueProcessor:
    """
    Processes and ranks teams in a league based on points and team name.

    Teams are sorted in descending order by points. Ties are broken alphabetically
    by team name. Teams with the same points receive the same rank.

    Attributes:
        sorted_teams (list[Team]): Sorted list of Team instances.

    Methods:
        set_ranks():
            Assigns ranks to teams based on their points, handling ties appropriately.
        
        get_league_results() -> str:
            Returns a newline-separated summary of the ranked teams.
    """

    def __init__(self, teams: list[Team]):
        """
        Initializes the LeagueProcessor with a list of Team objects.

        Args:
            teams (List[Team]): A list of Team instances. Each team must provide:
                - team_name (str)
                - points (int)
                - set_league_rank(rank: int)
                - league_rank (int)
                - get_summary() -> str
        """
        self.sorted_teams: list[Team] = sorted(
            teams,
            key=lambda team: (-team.points, team.team_name)
        )
        self._set_ranks()

    def get_league_results(self) -> str:
        """
        Returns:
            str: A newline-separated string representing the league standings.
        """
        return "\n".join(team.get_summary() for team in self.sorted_teams)

    def _set_ranks(self):
        """
        Assigns ranks to each team in the sorted list.
        Teams with equal points receive the same rank.
        """
        for i, team in enumerate(self.sorted_teams):
            if i == 0:
                team.set_league_rank(1)
            elif team.points == self.sorted_teams[i - 1].points:
                team.set_league_rank(self.sorted_teams[i - 1].league_rank)
            else:
                team.set_league_rank(i + 1)

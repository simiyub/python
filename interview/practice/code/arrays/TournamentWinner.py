"""
Requirement: For a given tournament, teams play in a round-robin with each team playing a match
against each of the other teams once.
There is always a winner and no ties in each match
and there has to be only one winner of the tournament.
You are required to determine the winner of the tournament given two arrays with:
Pairs of teams in each match
The results array where each entry matches the result of whether the home team won or not,
with a 0 indicating the home team lost and a 1 indicating they won.
Example: [[A, B], [A, C], [B, C]], [0, 0, 0]  - This implies Team C won because
team A lost to C as per second pair of teams and team B lost to C in the third pair of teams.

Implementation: We maintain a map of team and scores as well as the name of the team with the highest score.
When we get to the end of the array, we return the name of the team with the highest score.

Complexity: O(n) T, O(k) S as we iterate through the array once
and the store a map of teams (k) and their matching scores.
"""


def winner(competitions, results):
    def win(teams, score):
        return teams[0] if score == 1 else teams[1]

    def record_match(winning_team, scores):
        if winning_team not in scores:
            scores[winning_team] = 3
        else:
            scores[winning_team] += 3
        return scores

    tournament = {}
    current_leader = win(competitions[0], results[0])
    competitions = competitions[1:]
    tournament = record_match(current_leader, tournament)
    results = results[1:]

    for index in range(len(competitions)):
        competition = competitions[index]
        win = win(competition, results[index])
        tournament = record_match(win, tournament)
        if tournament[win] > tournament[current_leader]:
            current_leader = win
    return current_leader

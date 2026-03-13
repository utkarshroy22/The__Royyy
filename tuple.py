

cricket_matches = (("ICC World Cup Final 2024", "India", "Australia", 250, 240,
                    "India"), ("ICC World Cup Semi Final 1", "India",
                               "England", 280, 270, "India"),
                   ("ICC World Cup Semi Final 2", "South Africa", "Australia",
                    220, 230, "Australia"), ("ICC World Cup Quarter Final 1",
                                             "Pakistan", "New Zealand", 260,
                                             255, "Pakistan"),
                   ("ICC World Cup Quarter Final 2", "India", "Bangladesh",
                    300, 180, "India"), ("ICC World Cup Quarter Final 3",
                                         "Australia", "West Indies", 290, 200,
                                         "Australia"))


def calculate_match_margin(match):
    """Match ka winning margin calculate karna"""
    match_name, team1_name, team2_name, team1_runs, team2_runs, winner_team = match
    if winner_team == team1_name:
        return team1_runs - team2_runs
    else:
        return team2_runs - team1_runs


def get_team_statistics(all_matches, team_name):
    """Team ki total wins aur total runs calculate karna"""
    wins_count = 0
    total_runs_scored = 0

    for match in all_matches:
        match_name, team1_name, team2_name, team1_runs, team2_runs, winner_team = match
        if winner_team == team_name:
            wins_count += 1

        if team_name == team1_name:
            total_runs_scored += team1_runs
        elif team_name == team2_name:
            total_runs_scored += team2_runs

    return wins_count, total_runs_scored


print("=== ICC World Cup 2024 Complete Tournament Report ===")

print("All Matches Results:")
for match in cricket_matches:
    match_name, team1_name, team2_name, team1_runs, team2_runs, winner_team = match
    winning_margin = calculate_match_margin(match)
    print(f"{match_name}:")
    print(
        f"  {team1_name}: {team1_runs} runs vs {team2_name}: {team2_runs} runs"
    )
    print(f"  Winner: {winner_team} by {winning_margin} runs")

india_wins, india_total_runs = get_team_statistics(cricket_matches, "India")
print("India Complete Statistics:")
print(f"  Total Wins: {india_wins}")
print(f"  Total Runs Scored: {india_total_runs}")
print()

all_teams_wins = {}
for match in cricket_matches:
    winner_team_name = match[5]  # winner_team
    if winner_team_name in all_teams_wins:
        all_teams_wins[winner_team_name] += 1
    else:
        all_teams_wins[winner_team_name] = 1

print("All Teams Win Statistics (Highest to Lowest):")
sorted_teams = sorted(all_teams_wins.items(), key=lambda x: x[1], reverse=True)
for team_name, wins_count in sorted_teams:
    print(f"  {team_name}: {wins_count} wins")

highest_scoring_match = max(cricket_matches, key=lambda m: m[3] + m[4])
highest_total_runs = highest_scoring_match[3] + highest_scoring_match[4]

print(f"  {highest_scoring_match[0]}")
print(f"  Total Runs: {highest_total_runs} runs")

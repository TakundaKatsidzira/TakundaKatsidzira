import argparse
import csv
import ast
from collections import Counter, defaultdict

LOG_PATH = "../data/games_log.csv"

def parse_list(cell):
    try:
        return ast.literal_eval(cell)
    except:
        return []

def read_csv(filepath):
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

def analyze_games(log_path=LOG_PATH):
    data = read_csv(log_path)
    total_games = len(data)

    print(f"\n📊 Total games analyzed: {total_games}")

    # First player stats
    first_player_counts = Counter(row['first_player'] for row in data)
    print("\nFirst player counts:")
    for player in ('X', 'O'):
        count = first_player_counts[player]
        print(f"  {player}: {count} times ({count / total_games:.2%})")

    # Wins by player and who went first
    wins = Counter(row['winner'] for row in data)
    print("\nWin counts:")
    for p in ['X', 'O', 'Draw']:
        print(f"  {p}: {wins[p]} ({wins[p] / total_games:.2%})")

    # First player win rate
    fp_win_counts = Counter()
    for row in data:
        if row['winner'] == row['first_player']:
            fp_win_counts[row['first_player']] += 1

    print("\nFirst player win counts by player:")
    for p in ('X', 'O'):
        fp_total = first_player_counts[p]
        wins_as_first = fp_win_counts[p]
        print(f"  {p} went first and won {wins_as_first} out of {fp_total} games ({wins_as_first / fp_total:.2%})")

    total_fp_wins = sum(fp_win_counts.values())
    total_non_draws = total_games - wins['Draw']
    print(f"\nOverall first player win rate: {total_fp_wins / total_games:.2%}")
    print(f"First player wins (excluding draws): {total_fp_wins} out of {total_non_draws} games")

    # 🆕 Agent role and first player frequency
    print("\n🧍 Agent role and first player frequency:")
    role_counts = defaultdict(lambda: {'X': 0, 'O': 0, 'First': 0})
    for row in data:
        role_counts[row['agent_X_type']]['X'] += 1
        role_counts[row['agent_O_type']]['O'] += 1
        role_counts[row['agent_X_type' if row['first_player'] == 'X' else 'agent_O_type']]['First'] += 1

    print(f"{'Agent':<20} {'As X':>6} {'As O':>6} {'First':>6} {'Total':>7}")
    print("-" * 50)
    for agent, counts in sorted(role_counts.items()):
        x, o, first = counts['X'], counts['O'], counts['First']
        print(f"{agent:<20} {x:>6} {o:>6} {first:>6} {x + o:>7}")

    
    # Move stats
    move_counts = [len(parse_list(row['game_move_sequence'])) for row in data]
    avg_moves = sum(move_counts) / len(move_counts)
    print(f"\nAverage number of moves per game: {avg_moves:.2f}")
    print(f"Move sequence length: min {min(move_counts)}, max {max(move_counts)}, avg {avg_moves:.2f}")

    # First move positions
    first_moves = Counter(row['first_move'] for row in data)
    print("\nMost common first move positions:")
    for pos, count in first_moves.most_common(5):
        print(f"  Position {pos}: {count} times ({count / total_games:.2%})")

    
     # 🆕 Most common winning move (last move of winner)
    winning_moves = Counter()
    for row in data:
        if row['winner'] == 'Draw':
            continue
        sequence = parse_list(row['game_move_sequence'])
        if sequence:
            winning_moves[sequence[-1]] += 1
    print("\nMost common winning move positions:")
    for pos, count in winning_moves.most_common():
        print(f"  Position {pos}: {count} times")

    # Win methods (exclude draws)
    win_methods = Counter(row['win_method'] for row in data if row['winner'] != 'Draw')
    total_wins = total_games - wins['Draw']
    print("\nWin method distribution (excluding draws):")
    for method, count in win_methods.most_common():
        print(f"  {method}: {count} ({count / total_wins:.2%})")

    # New section: Unique move sequences
    print("\n🧬 Unique sequence diversity:")
    x_seqs = set()
    o_seqs = set()
    full_seqs = set()
    for row in data:
        x_seqs.add(tuple(parse_list(row['X_move_sequence'])))
        o_seqs.add(tuple(parse_list(row['O_move_sequence'])))
        full_seqs.add(tuple(parse_list(row['game_move_sequence'])))
    print(f"  Unique X Sequences:  {len(x_seqs)}")
    print(f"  Unique O Sequences:  {len(o_seqs)}")
    print(f"  Unique Full Games:   {len(full_seqs)}")

    # 🆕 Position usage frequency
    print("\nBoard position usage across all games:")
    position_counts = Counter()
    for row in data:
        sequence = parse_list(row['game_move_sequence'])
        position_counts.update(sequence)
    for i in range(9):
        count = position_counts[i]
        print(f"  Position {i}: {count} times ({count / total_games:.2f})")

    # Matchup analysis
    print("\nAgent matchups analysis:")
    matchups = defaultdict(list)
    for row in data:
        key = (row['agent_X_type'], row['agent_O_type'])
        matchups[key].append(row)

    for (agent_x, agent_o), games in sorted(matchups.items(), key=lambda x: -len(x[1])):
        count = len(games)
        x_wins = sum(1 for g in games if g['winner'] == 'X')
        o_wins = sum(1 for g in games if g['winner'] == 'O')
        draws = count - x_wins - o_wins
        avg_moves = sum(len(parse_list(g['game_move_sequence'])) for g in games) / count
        print(f"\nMatchup: {agent_x} vs {agent_o} - {count} games ({count / total_games:.2%})")
        print(f"  Wins for X: {x_wins} ({x_wins / count:.2%})")
        print(f"  Wins for O: {o_wins} ({o_wins / count:.2%})")
        print(f"  Draws:      {draws} ({draws / count:.2%})")
        print(f"  Average moves: {avg_moves:.2f}")

    
def main():
    parser = argparse.ArgumentParser(description="Analyze TicTacToe game logs.")
    parser.add_argument('--log', type=str, default=LOG_PATH, help='Path to games_log.csv')
    args = parser.parse_args()
    analyze_games(args.log)

if __name__ == "__main__":
    main()

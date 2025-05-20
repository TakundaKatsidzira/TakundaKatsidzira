import pandas as pd

def analyze_tictactoe_data(csv_path):
    # Load CSV
    df = pd.read_csv(csv_path, header=None, names=[
        'timestamp', 'first_player', 'winner', 'is_draw',
        'first_move_pos', 'move_sequence', 'num_moves', 'win_method'
    ])

    # Convert types
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['is_draw'] = df['is_draw'].astype(bool)
    df['first_move_pos'] = df['first_move_pos'].astype(int)
    df['num_moves'] = df['num_moves'].astype(int)
    df['win_method'] = df['win_method'].fillna('None')

    # Add first_player_won column
    df['first_player_won'] = (df['winner'] == df['first_player']) & (~df['is_draw'])

    total_games = len(df)
    print(f"Total games analyzed: {total_games}\n")

    # Count how many times each player went first
    first_player_counts = df['first_player'].value_counts()
    print("First player counts:")
    for player in ['X', 'O']:
        count = first_player_counts.get(player, 0)
        print(f"  {player}: {count} times ({count / total_games:.2%})")

    # Count first player wins for each first player identity
    print("\nFirst player win counts by player:")
    for player in ['X', 'O']:
        went_first_df = df[df['first_player'] == player]
        wins = went_first_df['first_player_won'].sum()
        total = len(went_first_df)
        print(f"  {player} went first and won {wins} out of {total} games ({(wins / total) if total > 0 else 0:.2%})")

    # Win counts including draws
    win_counts = df['winner'].value_counts()
    draws = df['is_draw'].sum()
    print("\nWin counts:")
    for player in ['X', 'O', 'None']:
        count = win_counts.get(player, 0) if player != 'None' else draws
        label = "Draws" if player == 'None' else player
        print(f"  {label}: {count} ({count / total_games:.2%})")

    # Win methods
    print("\nWin method distribution (excluding draws):")
    win_methods = df.loc[~df['is_draw'], 'win_method'].value_counts()
    for method, count in win_methods.items():
        print(f"  {method}: {count} ({count / (total_games - draws):.2%})")

    # First player win rate
    first_player_wins = df['first_player_won'].sum()
    print(f"\nOverall first player win rate: {first_player_wins / total_games:.2%}")
    print(f"First player wins (excluding draws): {first_player_wins} out of {total_games - draws} games")

    # Average number of moves
    avg_moves = df['num_moves'].mean()
    print(f"\nAverage number of moves per game: {avg_moves:.2f}")

    # Most common first moves
    common_first_moves = df['first_move_pos'].value_counts().head(5)
    print("\nMost common first move positions:")
    for pos, count in common_first_moves.items():
        print(f"  Position {pos}: {count} times ({count / total_games:.2%})")

    # Move sequence length stats
    move_seq_lengths = df['move_sequence'].apply(lambda s: len(s.split('-')))
    print(f"\nMove sequence length: min {move_seq_lengths.min()}, max {move_seq_lengths.max()}, avg {move_seq_lengths.mean():.2f}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python analyze_tictactoe_data.py path/to/dataset.csv")
    else:
        analyze_tictactoe_data(sys.argv[1])

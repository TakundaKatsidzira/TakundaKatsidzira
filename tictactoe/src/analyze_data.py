import pandas as pd
# Imports the pandas library, a powerful tool for data analysis and manipulation.
# Study: pandas basics (DataFrame, Series), data analysis in Python.

def analyze_tictactoe_data(csv_path):
    df = pd.read_csv(csv_path)
    # Loads the CSV file into a pandas DataFrame.
    # Study: Reading CSV files, DataFrame structure.

    # Convert types
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Converts the 'timestamp' column to datetime objects for easier time-based analysis.
    df['is_draw'] = df['is_draw'].astype(bool)
    # Ensures the 'is_draw' column is boolean (True/False).
    df['first_move_position'] = df['first_move_position'].astype(int)
    # Ensures the 'first_move_position' column is integer type.
    df['num_moves'] = df['num_moves'].astype(int)
    # Ensures the 'num_moves' column is integer type.
    df['win_method'] = df['win_method'].fillna('None')
    # Fills missing values in 'win_method' with the string 'None'.
    # Study: Data cleaning, type conversion, handling missing data in pandas.

    df['first_player_won'] = (df['winner'] == df['first_player']) & (~df['is_draw'])
    # Creates a new boolean column: True if the first player won and it wasn't a draw.
    # Study: Boolean indexing, creating new columns, logical operators.

    total_games = len(df)
    print(f"Total games analyzed: {total_games}\n")
    # Prints the total number of games in the dataset.
    # Study: len() function, f-strings for formatted output.

    # First player counts
    first_player_counts = df['first_player'].value_counts()
    # Counts how many times each player went first.
    print("First player counts:")
    for player in ['X', 'O']:
        count = first_player_counts.get(player, 0)
        print(f"  {player}: {count} times ({count / total_games:.2%})")
        # Prints how often each player went first, as a count and percentage.
        # Study: for loops, value_counts(), dictionary get(), f-strings, percentage formatting.

    # First player win counts by player
    print("\nFirst player win counts by player:")
    for player in ['X', 'O']:
        went_first_df = df[df['first_player'] == player]
        # Filters the DataFrame for games where this player went first.
        wins = went_first_df['first_player_won'].sum()
        # Sums up the number of wins for the first player.
        total = len(went_first_df)
        win_rate = (wins / total) if total > 0 else 0
        print(f"  {player} went first and won {wins} out of {total} games ({win_rate:.2%})")
        # Prints win statistics for each first player.
        # Study: DataFrame filtering, conditional expressions, division, f-strings.

    # Win counts including draws
    win_counts = df['winner'].value_counts()
    # Counts how many times each player won.
    draws = df['is_draw'].sum()
    # Counts the number of draws.
    print("\nWin counts:")
    for player in ['X', 'O', 'None']:
        count = win_counts.get(player, 0) if player != 'None' else draws
        label = "Draws" if player == 'None' else player
        print(f"  {label}: {count} ({count / total_games:.2%})")
        # Prints win/draw statistics.
        # Study: value_counts(), conditional logic, f-strings.

    # Win methods
    print("\nWin method distribution (excluding draws):")
    win_methods = df.loc[~df['is_draw'], 'win_method'].value_counts()
    # Filters out draws and counts win methods.
    total_wins = total_games - draws
    for method, count in win_methods.items():
        print(f"  {method}: {count} ({count / total_wins:.2%})")
        # Prints how each win method contributed to total wins.
        # Study: DataFrame filtering, value_counts(), for loops.

    # First player win rate
    first_player_wins = df['first_player_won'].sum()
    print(f"\nOverall first player win rate: {first_player_wins / total_games:.2%}")
    print(f"First player wins (excluding draws): {first_player_wins} out of {total_wins} games")
    # Prints overall win rate for the first player.
    # Study: Summing boolean columns, division, f-strings.

    # Average number of moves
    avg_moves = df['num_moves'].mean()
    print(f"\nAverage number of moves per game: {avg_moves:.2f}")
    # Prints the average number of moves per game.
    # Study: mean() function, column statistics.

    # Most common first moves
    common_first_moves = df['first_move_position'].value_counts().head(5)
    print("\nMost common first move positions:")
    for pos, count in common_first_moves.items():
        print(f"  Position {pos}: {count} times ({count / total_games:.2%})")
        # Prints the most common first moves.
        # Study: value_counts(), head(), for loops.

    # Move sequence length stats
    move_seq_lengths = df['move_sequence'].apply(lambda s: len(s.split('-')))
    print(f"\nMove sequence length: min {move_seq_lengths.min()}, max {move_seq_lengths.max()}, avg {move_seq_lengths.mean():.2f}")
    # Analyzes the length of move sequences (number of moves per game).
    # Study: apply(), lambda functions, string splitting, min/max/mean.

    # --- NEW: Analyze agent matchups ---
    print("\nAgent matchups analysis:")

    # Create a combined matchup label like "RandomAgent vs MinimaxAgent"
    df['matchup'] = df['agent_X'] + " vs " + df['agent_O']
    # Creates a new column combining agent types for X and O.
    # Study: String concatenation, creating new DataFrame columns.

    matchup_counts = df['matchup'].value_counts()
    for matchup, count in matchup_counts.items():
        print(f"\nMatchup: {matchup} - {count} games ({count / total_games:.2%})")
        # Prints the number of games for each agent matchup.

        subset = df[df['matchup'] == matchup]
        # Filters the DataFrame for this matchup.
        wins_X = (subset['winner'] == 'X').sum()
        wins_O = (subset['winner'] == 'O').sum()
        draws = subset['is_draw'].sum()
        print(f"  Wins for X: {wins_X} ({wins_X / count:.2%})")
        print(f"  Wins for O: {wins_O} ({wins_O / count:.2%})")
        print(f"  Draws: {draws} ({draws / count:.2%})")
        # Prints win/draw stats for this matchup.

        avg_moves_subset = subset['num_moves'].mean()
        print(f"  Average moves: {avg_moves_subset:.2f}")
        # Prints average moves for this matchup.
        # Study: DataFrame filtering, aggregation, statistics.

if __name__ == "__main__":
    import sys
    # Imports sys to access command-line arguments.
    if len(sys.argv) < 2:
        print("Usage: python analyze_tictactoe_data.py path/to/dataset.csv")
        # Prints usage instructions if no file is provided.
        # Study: sys.argv, command-line arguments, len().
    else:
        analyze_tictactoe_data(sys.argv[1])
        # Calls the analysis function with the provided CSV file path.
        # Study: Function calls, script entry points.

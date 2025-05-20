"""
Picture Grid Assignment
Transpose a list of lists and zero out the diagonal
"""

def transform(grid):
    # Transpose the grid
    rows, cols = len(grid), len(grid[0])
    transposed = [[grid[r][c] for r in range(rows)] for c in range(cols)]
    
    # Zero the diagonal (where row == col)
    for i in range(min(len(transposed), len(transposed[0]))):
        transposed[i][i] = 0

    # Print the result
    for row in transposed:
        print(row)

def main():
    # Example usage
    grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    transform(grid)

if __name__ == "__main__":
    main()

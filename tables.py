"""
Print Tables Assignment

Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume all inner lists have the same number of strings.
"""

def main():
    # Example data
    tableData = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]

    # Run the function
    printTable(tableData)

def printTable(table):
    # Number of columns (lists)
    col_count = len(table)
    # Number of rows (elements in each list)
    row_count = len(table[0])

    # Calculate the maximum width of each column
    col_widths = [max(len(item) for item in col) for col in table]

    # Print the table row by row
    for row in range(row_count):
        for col in range(col_count):
            print(table[col][row].rjust(col_widths[col]), end=' ')
        print()  # Newline after each row

if __name__ == "__main__":
    main()

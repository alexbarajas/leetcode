from typing import List


def matrixScore(grid: List[List[int]]) -> int:
    # 1. set up ROWS and COLUMNS
    ROWS = len(grid)
    COLUMNS = len(grid[0])

    # 2. if the first number in the row is 0, flip the row
    for row in range(ROWS):
        if grid[row][0] == 0:
            for column in range(COLUMNS):
                grid[row][column] = 1 if grid[row][column] == 0 else 0

    # 3. get the count of 1s in each column as an array
    column_count = [0 for j in range(COLUMNS)]
    for row in range(ROWS):
        for column in range(COLUMNS):
            column_count[column] += grid[row][column]

    # 4. if the count of 0 for a column is greater than the count of 1, flip the column
    for column in range(COLUMNS):
        if abs(column_count[column] - ROWS) > column_count[column]:
            for row in range(ROWS):
                grid[row][column] = 1 if not grid[row][column] else 0

    # 5. set answer as 0, go thru each row from the back, and calculate the binary number for that row
    answer = 0
    for row in range(ROWS):
        start = 0
        for column in range(COLUMNS - 1, -1, -1):
            start += 2 ** (COLUMNS - column - 1) if grid[row][column] else 0
        # 5.1. add the binary number from each row to answer
        answer += start

    # 6. return the answer
    return answer


print(matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == 39)
print(matrixScore([[0]]) == 1)
print(matrixScore([[0, 1], [1, 1]]) == 5)

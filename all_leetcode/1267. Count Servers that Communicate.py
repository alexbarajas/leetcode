from typing import List


def countServers(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLUMNS = len(grid[0])

    rows = [0] * ROWS
    columns = [0] * COLUMNS
    answer = 0

    for x in range(ROWS):
        for y in range(COLUMNS):
            if grid[x][y] == 1:
                rows[x] += 1
                columns[y] += 1
                answer += 1

    for x in range(ROWS):
        for y in range(COLUMNS):
            if grid[x][y] == 1 and rows[x] == 1 and columns[y] == 1:
                answer -= 1

    return answer


print(countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == 4)

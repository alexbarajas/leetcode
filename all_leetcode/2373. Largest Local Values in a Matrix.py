from typing import List


def largestLocal(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)

    answer = [[0 for j in range(n - 2)] for i in range(n - 2)]

    for row in range(1, n - 1):
        for column in range(1, n - 1):
            highest = 0
            for i in range(row - 1, row + 2):
                for j in range(column - 1, column + 2):
                    if grid[i][j] > highest:
                        highest = grid[i][j]
            answer[row - 1][column - 1] = highest

    return answer


print(largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]) == [[9, 9], [8, 6]])
print(largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]])

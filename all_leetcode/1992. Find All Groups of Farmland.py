from typing import List


def findFarmland(land: List[List[int]]) -> List[List[int]]:
    m = len(land)
    n = len(land[0])
    answer = []

    def dfs(start_x, start_y):
        end_x = start_x
        end_y = start_y
        while end_x < m - 1 and land[end_x + 1][end_y] == 1:
            end_x += 1
        while end_y < n - 1 and land[end_x][end_y + 1] == 1:
            end_y += 1
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                land[x][y] = 0
        answer.append([start_x, start_y, end_x, end_y])

    for row in range(m):
        for column in range(n):
            if land[row][column] == 1:
                dfs(row, column)

    return answer


print(findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]) == [[0, 0, 0, 0], [1, 1, 2, 2]])
print(findFarmland([[1, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0]]) == [[0, 0, 1, 1], [0, 5, 0, 5]])

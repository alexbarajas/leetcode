import collections
from typing import List


def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    ROWS = len(isWater)
    COLUMNS = len(isWater[0])
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = collections.deque()

    for x in range(ROWS):
        for y in range(COLUMNS):
            if isWater[x][y] == 1:
                queue.append((x, y, 0))
                isWater[x][y] = 0
            else:
                isWater[x][y] = -1

    while queue:
        for i in range(len(queue)):
            x, y, level = queue.popleft()
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < ROWS and 0 <= new_y < COLUMNS and isWater[new_x][new_y] == -1:
                    queue.append((new_x, new_y, level + 1))
                    isWater[new_x][new_y] = level + 1

    return isWater


print(highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]) == [[1, 1, 0], [0, 1, 1], [1, 2, 2]])

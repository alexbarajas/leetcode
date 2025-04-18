from typing import List


def maxDistance(position: List[int], m: int) -> int:
    n = len(position)
    position.sort()
    answer = 0

    def can_place_balls(gap):
        previous_ball_position = position[0]
        balls_placed = 1

        for i in range(1, n):
            if position[i] - previous_ball_position >= gap:
                previous_ball_position = position[i]
                balls_placed += 1

            if balls_placed == m:
                return True

        return False

    left = 1
    right = (position[-1] + position[0]) // (m - 1)  # if position=[1, 2, 3, 4, 7], m=3, right will be (7 + 1) // (3 - 1) = (8) // (2) = 4, so we will test up to a gap of 4
    while left <= right:
        midpoint = (right - left) // 2 + left
        if can_place_balls(midpoint):
            answer = midpoint
            left = midpoint + 1  # we shift left because we want to find the gap where the minimum magnetic force between any two balls is maximum
        else:
            right = midpoint - 1

    return answer


print(maxDistance(position=[1, 2, 3, 4, 7], m=3) == 3)
print(maxDistance(position=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], m=4) == 3)

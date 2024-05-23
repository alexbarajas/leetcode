from typing import List


def maxArea(height: List[int]) -> int:
    # 1. set up an answer variable, and also variables for left and right pointers
    answer = 0
    left = 0
    right = len(height) - 1

    # 2. while left <= right, calculate the current water level
    while left <= right:
        leftWater = height[left]
        rightWater = height[right]
        water = min(leftWater, rightWater) * (right - left)
        # 2.1. update the answer variable to be the max between the current answer and the current water level
        answer = max(answer, water)
        # 2.2. update the pointer that currently has the lower height
        if leftWater < rightWater:
            left += 1
        else:
            right -= 1

    # 3. return the answer
    return answer


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)

from typing import List


def findBuildings(heights: List[int]) -> List[int]:
    # # SOLUTION 1: uses an array from the back
    # max_height = 0
    # answer = []
    #
    # for i in range(len(heights) - 1, -1, -1):
    #     if heights[i] > max_height:
    #         answer.append(i)
    #         max_height = heights[i]
    #
    # return answer[::-1]

    # SOLUTION 2: uses a stack from the front
    stack = []
    for i in range(len(heights)):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        stack.append(i)

    return stack


print(findBuildings([4,2,3,1]) == [0, 2, 3])
print(findBuildings([2,2,2,2]) == [3])

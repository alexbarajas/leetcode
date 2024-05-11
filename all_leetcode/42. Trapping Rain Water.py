from typing import List


def trap(height: List[int]) -> int:
    # 0. base case to see if a height array exists
    if not height:
        return 0

    # 1. set up two pointers with their height as well, and an answer variable
    left = 0
    right = len(height) - 1
    leftWall = height[left]
    rightWall = height[right]
    answer = 0

    # 2. while left <= right you go thru the array
    while left <= right:
        # 3. if leftWall is less than rightWall, then add the max between 0 and the difference between leftWall minus height[left], set a new leftWall, and continue with left
        if leftWall < rightWall:
            answer += max(0, leftWall - height[left])
            leftWall = max(leftWall, height[left])
            left += 1

        # 3.1 if not then do the same but for rightWall
        else:
            answer += max(0, rightWall - height[right])
            rightWall = max(rightWall, height[right])
            right -= 1

    # 4. return the answer array
    return answer

    # # this could also work for the while loop, where you add to the answer at first and then change the pointers
    # while left <= right:
    #     answer += ((leftWall - height[left]) + (rightWall - height[right]))
    #     if leftWall < rightWall:
    #         left += 1
    #         leftWall = max(leftWall, height[left])
    #     else:
    #         right -= 1
    #         rightWall = max(rightWall, height[right])
    # return answer


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6)
print(trap([4, 2, 0, 3, 2, 5]) == 9)

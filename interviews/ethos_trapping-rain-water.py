
def trap(height):
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

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
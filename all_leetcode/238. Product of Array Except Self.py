from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    # 1. set up n, the answer array, as well as the left and right pointers, set all values to 1
    n = len(nums)
    answer = [1 for _ in range(n)]
    left = 1
    right = 1

    # 2. go thru the array, multiply the values in the answer array with the pointers first, and then get new values for left and right
    for i in range(n):
        answer[i] *= left
        answer[n - i - 1] *= right
        left *= nums[i]
        right *= nums[n - i - 1]

    # 3. return the answer array
    return answer


print(productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
print(productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])

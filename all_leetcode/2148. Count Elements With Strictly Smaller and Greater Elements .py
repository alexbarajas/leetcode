from typing import List


def countElements(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0

    minimum = float("inf")
    minimum_count = 0
    maximum = float("-inf")
    maximum_count = 0

    for num in nums:
        if num < minimum:
            minimum = num
            minimum_count = 1
        elif num == minimum:
            minimum_count += 1
        if num > maximum:
            maximum = num
            maximum_count = 1
        elif num == maximum:
            maximum_count += 1

    return max(0, n - maximum_count - minimum_count)


print(countElements([11, 7, 2, 15]) == 2)
print(countElements([-3, 3, 3, 90]) == 2)

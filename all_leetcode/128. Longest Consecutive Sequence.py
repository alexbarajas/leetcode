from typing import List


def longestConsecutive(nums: List[int]) -> int:
    length = 0
    nums = set(nums)
    # nums = {1, 2, 3, 4, 100, 200}

    for num in nums:
        if num - 1 not in nums:  # starts from each sequence and moves upwards
            currentNum = num
            while currentNum in nums:
                currentNum += 1
            length = max(length, currentNum - num)

    return length


print(longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)

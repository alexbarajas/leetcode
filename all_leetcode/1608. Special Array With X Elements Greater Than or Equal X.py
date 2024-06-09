from typing import List


def specialArray(nums: List[int]) -> int:
    # set up all the possible values that can be valid in a counts array
    counts = [0 for i in range(len(nums) + 1)]
    n = len(counts)

    # go thru each num in nums, starting from x = 1, while x < n and x <= num, incrementing counts[x] and x as you go along
    for num in nums:
        x = 1
        while x < n and x <= num:
            counts[x] += 1
            x += 1

    # once counts has been filled up, go thru it and if counts[i] == i return i
    for i in range(1, n):
        if counts[i] == i:
            return i

    # otherwise, at the end return -1
    return -1


print(specialArray([3, 5]) == 2)

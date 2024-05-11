from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        num = nums[i]
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i


print(twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1])
print(twoSum(nums=[3, 2, 4], target=6) == [1, 2])

from typing import List


def countBadPairs(nums: List[int]) -> int:
    # hashmap = {}
    # answer = 0

    # for i in range(len(nums)):
    #     answer += i - hashmap[nums[i] - i] if nums[i] - i in hashmap else i
    #     # if nums[i] - i in hashmap:
    #     #     answer += i - hashmap[nums[i] - i]
    #     # else:
    #     #     answer += i
    #     hashmap[nums[i] - i] = hashmap.get(nums[i] - i, 0) + 1

    # return answer

    # SOLUTION 3: start from the back
    hashmap = {}
    answer = 0

    for i in range(len(nums) - 1, -1, -1):
        num = i - nums[i]
        answer += i - (hashmap[num] if num in hashmap else 0)
        hashmap[num] = hashmap.get(num, 0) + 1

    return answer


print(countBadPairs([4, 1, 3, 3]) == 5)

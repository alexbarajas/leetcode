from typing import List


def isArraySpecial(nums: List[int], queries: List[List[int]]) -> List[bool]:
    current_section = 0
    num_locations = {0: 0}

    for i in range(1, len(nums)):
        if nums[i - 1] % 2 == nums[i] % 2:
            current_section += 1
        num_locations[i] = current_section

    answer = []
    for x, y in queries:
        answer.append(num_locations[x] == num_locations[y])

    return answer


print(isArraySpecial(nums=[3, 4, 1, 2, 6], queries=[[0, 4]]) == [False])
print(isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]) == [False, True])

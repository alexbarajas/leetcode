from typing import List


def maximumSum(nums: List[int]) -> int:
    # SOLUTION 1: hashmap
    hashmap = {}
    answer = -1

    for num in nums:
        digit_sum = 0
        for digit in str(num):
            digit_sum += int(digit)
        if digit_sum in hashmap:
            answer = max(answer, num + hashmap[digit_sum])
        hashmap[digit_sum] = max(hashmap.get(digit_sum, 0), num)

    return answer

    # # SOLUTION 2: array
    # array = [0] * 82
    # answer = -1

    # for num in nums:
    #     digit_sum = 0
    #     for digit in str(num):
    #         digit_sum += int(digit)
    #     if array[digit_sum]:
    #         answer = max(answer, num + array[digit_sum])
    #     array[digit_sum] = max(num, array[digit_sum])

    # return answer


print(maximumSum([18, 43, 36, 13, 7]) == 54)
print(maximumSum([10, 12, 19, 14]) == -1)

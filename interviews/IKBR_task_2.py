"""
given an array A of N integers, return max sum of 2 numbers whose digits
add up to an equal sum. if no pairs then return -1.
"""


def solution(A):
    hashmap = {}
    count = 0
    for num in A:
        sum_digits = sum(int(digit) for digit in str(num))
        if sum_digits not in hashmap:
            hashmap[sum_digits] = [num]
        else:
            if len(hashmap[sum_digits]) == 2:
                min_value = min(hashmap[sum_digits])
                if num > min_value:
                    hashmap[sum_digits].remove(min_value)
                    hashmap[sum_digits].append(num)
            else:
                hashmap[sum_digits].append(num)
                count += 1
    if count == 0:
        return -1
    else:
        for sum_digits in hashmap:
            if len(hashmap[sum_digits]) > 1:
                hashmap[sum_digits] = sum(hashmap[sum_digits])
            else:
                hashmap[sum_digits] = 0
        return max(hashmap.values())




    # hmap = {}  # vighnesh solution
    # for num in A:
    #     sum_of_digits = sum(int(digit) for digit in str(num))
    #     if sum_of_digits in hmap:
    #         if len(hmap[sum_of_digits]) > 1:
    #             min_num = min(hmap[sum_of_digits])
    #             if num > min_num:
    #                 hmap[sum_of_digits].remove(min_num)
    #                 hmap[sum_of_digits].append(num)
    #         else:
    #             hmap[sum_of_digits].append(num)
    #     else:
    #         hmap[sum_of_digits] = [num]
    #
    # res = -1
    # for pairs in hmap.values():
    #     if len(pairs) != 2:
    #         continue
    #
    #     res = max(res, pairs[0] + pairs[1])
    # print(hmap)
    # return res


A = [51, 71, 17, 42]
print(solution(A))

A = [42, 33, 60]
print(solution(A))

A = [51, 32, 43]
print(solution(A))

A = [51, 32, 43, 14]
print(solution(A))

from typing import List


def countCompleteDayPairs(hours: List[int]) -> int:
    hashmap = {}
    answer = 0

    for num in hours:
        num = 24 if num % 24 == 0 else num % 24
        if 24 - (num % 24) in hashmap:
            answer += hashmap.get(24 - (num % 24), 0)
        hashmap[num] = hashmap.get(num, 0) + 1

    return answer


print(countCompleteDayPairs([12, 12, 30, 24, 24]) == 2)

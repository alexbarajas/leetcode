from typing import List

"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""


def numRescueBoats(people: List[int], limit: int) -> int:
    # 1. sort the people array, and make left and right pointers, along with an answer variable
    people.sort()
    left = 0
    right = len(people) - 1
    answer = 0

    # 2. go thru the array, adding 1 to answer each time
    while left <= right:
        answer += 1
        # 3. if the left and right people can share a boat, then move left by 1, move right by 1 each turn regardless
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1

    # 4. return the answer
    return answer


print(numRescueBoats(people=[1, 2], limit=3) == 1)
print(numRescueBoats(people=[5, 1, 4, 2], limit=6) == 2)

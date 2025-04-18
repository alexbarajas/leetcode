from typing import List


def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    n = len(customers)
    answer = 0

    current_angry = 0
    max_angry = 0

    left = 0
    for right in range(n):
        current_angry += customers[right] * grumpy[right]
        if right - left == minutes:
            current_angry -= customers[left] * grumpy[left]
            left += 1
        if current_angry > max_angry:
            max_angry = current_angry
        answer += customers[right] * (1 - grumpy[right])

    return answer + max_angry


print(maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3) == 16)
print(maxSatisfied(customers=[1], grumpy=[0], minutes=1) == 1)

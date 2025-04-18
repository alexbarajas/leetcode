from typing import List


def minDays(bloomDay: List[int], m: int, k: int) -> int:
    if m * k > len(bloomDay):
        return -1

    def get_num_of_bouquets(midpoint):
        number_of_bouquets = 0
        consecutive_flowers = 0

        for day in bloomDay:
            if day <= midpoint:
                consecutive_flowers += 1
            else:
                consecutive_flowers = 0

            if consecutive_flowers == k:
                number_of_bouquets += 1
                consecutive_flowers = 0

        return number_of_bouquets

    min_days = -1

    left = float("inf")
    right = float("-inf")
    for flower in bloomDay:
        left = min(left, flower)
        right = max(right, flower)

    while left <= right:
        midpoint = (right - left) // 2 + left
        if get_num_of_bouquets(midpoint) >= m:
            min_days = midpoint
            right = midpoint - 1
        else:
            left = midpoint + 1

    return min_days


print(minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1) == 3)
print(minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2) == -1)
print(minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3) == 12)

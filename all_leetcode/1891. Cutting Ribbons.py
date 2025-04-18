from typing import List


def maxLength(ribbons: List[int], k: int) -> int:
    left = 0  # technically a ribbon can't be of length 0, but 0 is still a possible answer so we start this as 0
    right = max(ribbons)  # the largest length a ribbon could have

    def is_possible(length):
        total_ribbons = 0
        for ribbon in ribbons:
            total_ribbons += ribbon // length
            if total_ribbons >= k:
                return True
        return False

    while left < right:
        # the reason we do (right - left + 1) instead of (right - left) is because,
        # when we move the left bound of the binary search to the value of midpoint to search for the higher range,
        # in order to avoid an infinite loop when left is updated to midpoint, we need to make sure midpoint is different,
        # so using midpoint = (right - left + 1) // 2 + left allows us to do that
        midpoint = (right - left + 1) // 2 + left
        # print(left, right, midpoint)
        if is_possible(midpoint):
            left = midpoint
        else:
            right = midpoint - 1

    return left


print(maxLength(ribbons=[9, 7, 5], k=3))

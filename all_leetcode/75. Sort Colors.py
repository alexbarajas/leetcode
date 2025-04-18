from typing import List


def sortColors(nums: List[int]) -> List[int]:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    pointer0 = 0
    pointer2 = n - 1

    current = 0
    while current <= pointer2:  # we do while current is <= pointer2 because once we reach pointer2, every value including that and past it is a 2 already
        # if the current value is 0, switch it with the pointer0 value to ensure that 0 goes to the front
        if nums[current] == 0:
            nums[pointer0], nums[current] = nums[current], nums[pointer0]
            pointer0 += 1
            current += 1
        # if the current value is 2, switch it with the pointer2 value to ensure that 0 goes to the back
        elif nums[current] == 2:
            nums[current], nums[pointer2] = nums[pointer2], nums[current]
            pointer2 -= 1
            # you don't increment current here because the value at the new nums[current] will have to be looked at again, the 2 has been shifted to the end so the array window got smaller anyway
        else:
            current += 1

    return nums


print(sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2])

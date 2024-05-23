from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # 1. base case if len(nums) < 3 return an empty array
    n = len(nums)
    if n < 3:
        return []

    # 2. set up an empty answer array and then sort the nums array
    answer = []
    nums.sort()

    # 3. go thru each value a in the nums array up to nums[n - 2]
    for a in range(n - 2):
        # 3.1 if a > 0 and nums[a] == nums[a - 1], just continue in the loop
        if a > 0 and nums[a] == nums[a - 1]:
            continue

        # 3.2 set up the b and c pointer values and move thru the array until b !< c
        b = a + 1
        c = n - 1

        while b < c:
            # 3.3 if you find a match, add it to the array, add 1 to b, and then check if there are duplicates of b doing the same you did above in the loop
            if nums[a] + nums[b] + nums[c] == 0:
                answer.append([nums[a], nums[b], nums[c]])
                b += 1
                while nums[b] == nums[b - 1] and b < c:
                    b += 1
            elif nums[a] + nums[b] + nums[c] < 0:
                b += 1
            else:
                c -= 1

    # 4. return the answer array
    return answer


print(threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
print(threeSum([0, 1, 1]) == [])

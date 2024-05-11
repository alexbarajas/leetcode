from typing import List


def maximumSubarraySum(nums: List[int], k: int) -> int:
    # 0. base case: set answer as 0, if k is larger than the length of nums return answer
    answer = 0
    n = len(nums)
    if k > n:
        return answer

    # 1. set up an empty hashset and a total variable, you use the total variable instead of doing sum(hashset) because you don't want to calculate the sum of the hashset for when k is a very large number
    hashset = set()
    total = 0

    # 2. use a sliding window with a max size of k
    left = 0
    for right in range(n):
        number = nums[right]
        # 2.1. if the current number is in the hashset, shift left until it isn't by removing nums[left] from the hashset, and incrementing left and decrementing the total as you do it
        if number in hashset:
            while number in hashset:
                total -= nums[left]
                hashset.remove(nums[left])
                left += 1
            total += number
            hashset.add(number)
        # 2.2. if the current number is not in the hashset, add it to the hashset and increment total
        else:
            total += number
            hashset.add(number)
            # 2.2.1. if the sliding window has reached a size of k, change answer if needed, and update total and the hashset since you're incrementing left
            if right - left + 1 == k:
                answer = max(answer, total)
                total -= nums[left]
                hashset.remove(nums[left])
                left += 1

    # 3. return the answer
    return answer


print(maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3) == 15)
print(maximumSubarraySum(nums=[4, 4, 4], k=3) == 0)

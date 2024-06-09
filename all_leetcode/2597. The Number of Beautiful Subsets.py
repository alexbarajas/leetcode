def beautifulSubsets(nums, k) -> int:
    # SOLUTION 1: easy to understand
    nums.sort()
    n = len(nums)
    answer = [0]

    def backtracking(current_values, start):
        if current_values:
            answer[0] += 1
        for i in range(start, n):
            if not current_values or (nums[i] - k not in current_values):
                current_values[nums[i]] = current_values.get(nums[i], 0) + 1
                backtracking(current_values, i + 1)
                current_values[nums[i]] -= 1
                if current_values[nums[i]] == 0:
                    current_values.pop(nums[i])

    backtracking({}, 0)

    return answer[0]

    # # SOLUTION 2: more efficient
    # nums.sort()
    # n = len(nums)
    # answer = [0]
    #
    # def backtracking(current_values, start):
    #     if start == n:
    #         return
    #     for i in range(start, n):
    #         if nums[i] - k not in current_values:
    #             answer[0] += 1
    #             current_values[nums[i]] = current_values.get(nums[i], 0) + 1
    #             backtracking(current_values, i + 1)
    #             current_values[nums[i]] -= 1
    #             if current_values[nums[i]] == 0:
    #                 current_values.pop(nums[i])
    #
    # backtracking({}, 0)
    #
    # return answer[0]



print(beautifulSubsets(nums=[2, 4, 6], k=2) == 4)
print(beautifulSubsets(
    nums=[1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
          1000, 1000], k=1) == 1048575)
print(beautifulSubsets(nums=[10, 4, 5, 7, 2, 1], k=3) == 23)
print(beautifulSubsets(
    nums=[183, 104, 696, 699, 631, 562, 654, 79, 518, 77, 469, 806, 525, 487, 84, 707, 880, 21, 463, 212], k=504) == 786431)

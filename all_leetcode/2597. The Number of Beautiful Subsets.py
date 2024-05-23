def beautifulSubsets(nums, k) -> int:
    nums.sort()
    n = len(nums)
    answer = [0]

    def backtracking(current_values, current_indices, start):
        if current_values:
            answer[0] += 1
        for i in range(start, n):
            if not current_values or (nums[i] - k not in current_values):
                current_values[nums[i]] = current_values.get(nums[i], 0) + 1
                current_indices.add(i)
                backtracking(current_values, current_indices, i + 1)
                current_values[nums[i]] = current_values.get(nums[i], 0) - 1
                current_indices.remove(i)
                if current_values[nums[i]] == 0:
                    current_values.pop(nums[i])

    backtracking({}, set(), 0)

    return answer[0]


print(beautifulSubsets(nums=[2, 4, 6], k=2) == 4)
print(beautifulSubsets(
    nums=[1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
          1000, 1000], k=1) == 1048575)
print(beautifulSubsets(nums=[10, 4, 5, 7, 2, 1], k=3) == 23)
print(beautifulSubsets(
    nums=[183, 104, 696, 699, 631, 562, 654, 79, 518, 77, 469, 806, 525, 487, 84, 707, 880, 21, 463, 212], k=504) == 786431)

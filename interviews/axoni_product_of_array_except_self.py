def productExceptSelf(nums):
    # 0. base case if there is no nums
    if not nums:
        return None

    # 1. set up a base case if len(nums) < 2 to return 0
    length = len(nums)
    if length < 2:
        return 0

    # 2. set up the answer array, as well as the left and right pointers, set all values to 1
    answer = [1 for _ in range(length)]
    left = 1
    right = 1

    # 3. go thru the array, multiply the values in the answer array with the pointers first, and then get new values for left and right
    for i in range(length):
        answer[i] *= left
        answer[length - i - 1] *= right
        left *= nums[i]
        right *= nums[length - i - 1]

    # 4. return the answer array
    return answer


nums = [1,2,3,4]
print(productExceptSelf(nums))


from typing import List
def findLonely(nums: List[int]) -> List[int]:
    # 1. make a counts hashmap, and make an answer array
    counts = {}
    answer = []

    # 2. get the count for each number into the counts hashmap
    for number in nums:
        counts[number] = counts.get(number, 0) + 1

    # 3. go through the counts hashmap, if the count is over 1, continue, if the neighbors are not in the hashmap, add it to the answer array
    for number, count in counts.items():
        if count == 1 and number - 1 not in counts and number + 1 not in counts:
            answer.append(number)

    # 4. return the answer array
    return answer

print(findLonely([10,6,5,8]) == [10, 8])

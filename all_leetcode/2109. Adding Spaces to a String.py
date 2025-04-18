from typing import List

def addSpaces(s: str, spaces: List[int]) -> str:
    answer = ""
    left = 0

    for i in range(len(spaces)):
        current = spaces[i] + i
        answer += s[left: current - i] + " "
        left = current - i

    return answer + s[left:]

print(addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]) == "Leetcode Helps Me Learn")

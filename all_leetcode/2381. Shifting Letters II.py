from typing import List

def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    n = len(s)
    netShifts = [0 for i in range(n)]

    for start, end, direction in shifts:
        netShifts[start] += 1 if direction else -1
        # the reason why we do the opposite for end + 1 instead of doing something for end is because end will continue the prefixSum trend from the values before it, while end + 1 will essentially exit out of the current trend from the given shift, and for this it needs to reverse the change that the shift made
        if end < n - 1:
            netShifts[end + 1] -= 1 if direction else -1

    prefixSum = 0
    answer = []
    for i in range(n):
        prefixSum += netShifts[i]
        netShift = (prefixSum % 26 + 26) % 26
        answer.append(chr((ord(s[i]) - ord('a') + netShift) % 26 + ord('a')))

    return ''.join(answer)

print(shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]]) == "catz")

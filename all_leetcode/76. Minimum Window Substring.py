import collections


def minWindow(s: str, t: str) -> str:
    # 0. base case if t is larger than s
    if not s or not t or len(t) > len(s):
        return ""

    # 1. set up an empty hashmap for countS and a Counter hashmap for countT
    countS = {}
    countT = collections.Counter(t)

    # 2. set up your have and need variables for the letters you need to satisfy, along with your answer and answerLength variables
    have = 0
    need = len(countT)  # letters that you need to be full
    answer = [-1, -1]
    answerLength = float("inf")

    # 3. using 2 pointers, start left at 0, and go thru s using right
    left = 0
    for right in range(len(s)):
        # 3.1. add each letter to countS as you see them with their count
        letter = s[right]
        # 3.2. if the letter count is the same in countS and countT, have += 1
        countS[letter] = countS.get(letter, 0) + 1
        # 3.3. check if you can add 1 more to have by seeing if letter in countT and countS[letter] == countT[letter]
        if letter in countT and countT[letter] == countS[letter]:
            have += 1
            # 3.3.1. while have == need, update the answer, and answerLength, then start reducing from countS until have != need, shift left each time
            while have == need:
                # first check the window size and modify the answer if needed
                if (right - left + 1) < answerLength:  # check to see if you can get a new minimum window size
                    answerLength = right - left + 1
                    answer = [left, right]
                # then shift left and remove from countS and modify the have variable if needed
                countS[s[left]] -= 1
                if countS[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

    # 4. if the answerLength is not infinite, return the array that answer corresponds to, otherwise return ""
    return s[answer[0]: answer[1] + 1] if answerLength != float("inf") else ""


print(minWindow(s="ADOBECODEBANC", t="ABC") == "BANC")
print(minWindow(s="a", t="aa") == "")

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    answer = ""
    if len(strs) == 1:
        return strs[0]

    for i in range(min(len(word) for word in strs)):
        start = strs[0][i]
        for word in strs[1:]:
            if word[i] != start:
                return word[:i]
        answer += start

    return answer


print(longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(longestCommonPrefix(["ab", "a"]) == "a")
print(longestCommonPrefix(["", ""]) == "")

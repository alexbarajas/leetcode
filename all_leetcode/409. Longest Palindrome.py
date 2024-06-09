
def longestPalindrome(s: str) -> int:
    # # SOLUTION 1: uses a hashmap
    # answer = 0
    # odd = False

    # hashmap = collections.Counter(s)

    # for count in sorted(hashmap.values(), reverse=True):
    #     if count % 2 == 1:
    #         if not odd:
    #             odd = True
    #         else:
    #             answer -= 1
    #     answer += count

    # return answer

    # SOLUTION 2: this is cleaner
    evens = 0
    odds = set()

    for character in s:
        if character in odds:
            evens += 1
            odds.remove(character)
        else:
            odds.add(character)

    return evens * 2 + (1 if odds else 0)


print(longestPalindrome("abccccdd") == 7)

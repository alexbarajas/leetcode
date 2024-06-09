def wordPatternMatch(pattern: str, s: str) -> bool:
    n_p = len(pattern)
    n_s = len(s)
    hashmap = {}  # to check if characters in pattern have not been seen
    seen = set()  # to check if characters in s have not been seen

    def backtracking(p_i, s_i):
        # the base case where you reach the end of the pattern
        if p_i == n_p:
            return s_i == n_s
        # get the current pattern character
        character = pattern[p_i]
        # if the current character already has a word in hashmap, check to see if it fits the current pattern in s, if not return False, otherwise keep on recursively
        if character in hashmap:
            word = hashmap[character]
            if s[s_i: s_i + len(word)] != word:
                return False
            return backtracking(p_i + 1, s_i + len(word))
        # if the current character is not in the hashmap, then you need to create a new word for every possible combination for the rest of s using a for loop
        for k in range(s_i + 1, n_s + 1):
            # the new_word will go from s_i until k which can go from s_i + 1 until the end of s
            new_word = s[s_i: k]
            # if that new_word has been seen already, then continue to the next possible new_word
            if new_word in seen:
                continue
            # add/update the current character in the hashmap with the new_word, and add new_word to the seen hashset
            hashmap[character] = new_word
            seen.add(new_word)
            # initiate backtracking with the next index in p, and s_i + len(new_word) since you're backtracking with that new_word, if this instance is True then return True
            if backtracking(p_i + 1, s_i + len(new_word)):
                return True
            # remove that new_word to the hashmap with the character as the key, and to the seen hashset
            seen.remove(new_word)
            hashmap.pop(character)

    # return the backtracking function starting from (0, 0)
    return backtracking(0, 0)


print(wordPatternMatch(pattern="abab", s="redblueredblue"))
print(wordPatternMatch(pattern="aaaa", s="asdasdasdasd"))
print(not wordPatternMatch(pattern="aabb", s="xyzabcxzyabc"))

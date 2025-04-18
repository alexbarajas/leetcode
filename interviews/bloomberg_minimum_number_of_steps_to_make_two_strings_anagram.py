
def minSteps(s: str, t: str) -> int:
    # 0. base case
    if len(s) != len(t):
        raise

    # 1. set up the answer variable as 0
    answer = 0

    # 2. set up the hashmaps to have the count of each letter in each input
    s_map = {}
    for letter in s:
        if not letter.isalpha():
            raise
        s_map[letter] = s_map.get(letter, 0) + 1
    t_map = {}
    for letter in t:
        if not letter.isalpha():
            raise
        t_map[letter] = t_map.get(letter, 0) + 1

    # 3. go thru the hashmap and see which letters are the same
    for letter, count in s_map.items():
        # 3.1. if a letter is not in t_map, add the count to the answer
        if letter not in t_map:
            answer += count
        else: # 3.2 if letter is in t_map, add the difference between counts to the answer
            if s_map[letter] > t_map[letter]:
                answer += abs(s_map[letter] - t_map[letter])

    # 4. return answer
    return answer

s = "bab"
t = "aba"

print(minSteps(s, t))
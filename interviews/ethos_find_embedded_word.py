# You are running a classroom and suspect that some of your students are passing around the answers to multiple choice questions disguised as random strings.

# Your task is to write a function that, given a list of words and a string, finds and returns the word in the list that is scrambled up inside the string, if any exists. There will be at most one matching word. The letters don't need to be in order or next to each other. The letters cannot be reused.

# Example:
# words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
# string1 = 'tcabnihjs'
# find_embedded_word(words, string1) -> cat (the letters do not have to be in order)

# string2 = 'tbcanihjs'
# find_embedded_word(words, string2) -> cat (the letters do not have to be together)

# string3 = 'baykkjl'
# find_embedded_word(words, string3) -> None / null (the letters cannot be reused)

# string4 = 'bbabylkkj'
# find_embedded_word(words, string4) -> baby

# string5 = 'ccc'
# find_embedded_word(words, string5) -> None / null

# string6 = 'breadmaking'
# find_embedded_word(words, string6) -> bird

def find_embedded_word(words, string):
    # make a hashmap with the counts of each letter in the string
    string_count = {}
    for letter in range(len(string)):
        string_count[string[letter]] = string_count.get(string[letter], 0) + 1

    for word in words:
        word_count = {}
        # create a hashmap with the counts of each letter in the word
        for letter in range(len(word)):
            word_count[word[letter]] = word_count.get(word[letter], 0) + 1

        for letter, count in word_count.items():
            if letter in string_count:
                word_count[letter] -= string_count[letter]

        if max(word_count.values()) <= 0:
            return word

    return None


words = ["cat", "baby", "dog", "bird", "car", "ax"]
string1 = "tcabnihjs"  # cat
string2 = "tbcanihjs"  # cat
string3 = "baykkjl"  # None
string4 = "bbabylkkj"  # baby
string5 = "ccc"  # None
string6 = "breadmaking"  # bird

print(find_embedded_word(words, string1))
print(find_embedded_word(words, string2))
print(find_embedded_word(words, string3))
print(find_embedded_word(words, string4))
print(find_embedded_word(words, string5))
print(find_embedded_word(words, string6))
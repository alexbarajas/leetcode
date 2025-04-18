"""
3. how many sentences?
"""


def countSentences(wordSet, sentences):
    # 1. set up a hashmap to get the possible combinations for each word in the wordSet, along with an answer variable as 1
    hashmap = {}
    answer = 1
    # 2. for each word in wordSet, put the sorted string in the hashmap along with the count for that sorted string
    for word in wordSet:
        string = "".join(sorted(word))
        hashmap[string] = hashmap.get(string, 0) + 1
        answer *= (hashmap[string] ** 2)
    # 3. once the hashmap for each sorted string and their count is full, go through each word in the sentence,
    # and multiply the answer by the value corresponding to each key (sorted word)
    # for word in sentences.split():
    #     answer *= hashmap["".join(sorted(word))]
    # 4. finally return the answer value
    return answer


wordSet = ["listen", "silent", "it", "is"]
sentences = "listen it is silent"

print(countSentences(wordSet, sentences))

wordSet = ["cat", "the", "bats"]
sentences = "cat the bats"

print(countSentences(wordSet, sentences))

# THIS WAS WRONG BECAUSE OF TIME LIMIT EXCEEDED, IDK HOW, BUT OPTIMIZE IT


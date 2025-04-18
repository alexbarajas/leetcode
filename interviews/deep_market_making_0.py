"""
How many words are in a given sentence?

s = "How many eggs are in a half-dozen, 13?"
7 words
"""




def howMany(sentence):
    count = 0  # counter for our words
    symbols = "@#$%^&*()+_=<>/\"[]{}"  # list of all applicable symbols
    for word in sentence.split(" "):  # splits up the string into individual words
        for character in word:  # goes through each character in each word and checks it
            if character.isdigit() or character in symbols:
                count -= 1
                break
        if word == "":  # gets rid of blanks
            count -= 1
        count += 1
    return count


sentence = "How many eggs are in a half-dozen, 13?"
print(howMany(sentence))

sentence = "jds dsaf lkdf kdsa fkldsf, adsbf ldka ads? asd bfdal ds bf[l. akf dhj ds 878  dwa WE DE 7475 dsfh ds  RAMU 748 dj."
print(howMany(sentence))

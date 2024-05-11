def reversePrefix(word: str, ch: str) -> str:
    index = 0
    for i in range(len(word)):
        if word[i] == ch:
            index = i
            break

    # this line can replace the lines below
    return word[:index + 1][::-1] + word[index + 1:]

    # answer = []
    # for j in range(len(word)):
    #     if j <= index:
    #         answer.append(word[index - j])
    #     else:
    #         answer.append(word[j])

    # return "".join(answer)


print(reversePrefix(word="abcdefd", ch="d") == "dcbaefd")

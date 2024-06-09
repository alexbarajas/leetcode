# notes: readability, just focus on solution, efficiency later, not designed to be finished, can search

# "1 + 2 + 3 + 1" ⇒ 7
# given a string of an addition expression, return the result

# first question
def addition(s):
    n = len(s)
    answer = 0
    i = 0
    while i < n:
        if s[i] == "-":
            if s[i + 1].isnumeric():
                start = i + 1
                end = i + 1
                while end < n - 1 and s[end + 1].isnumeric():
                    end += 1
                integer = int(s[start: end + 1])
                answer -= integer
                i = end + 1
        elif s[i].isnumeric():
            start = i
            end = i
            while end < n - 1 and s[end + 1].isnumeric():
                end += 1
            integer = int(s[start: end + 1])
            answer += integer
            i = end + 1
        i += 1
    return answer


print(addition("1 + 2 + 3 + 1") == 7)
print(addition("-10 + 2 + 3 + 1") == -4)


# "-10 + 4 / 2 * 3" == -4

# stack = [-10, "+", 4, "/", 2, "*", 3]
# stack = [-10, "+", 6]
# stack = [-4]

# second question
def calculator(s):
    n = len(s)
    stack = []
    i = 0
    # creates initial stack
    while i < n:
        character = s[i]
        if character in "+*/":
            stack.append(character)
        elif character == "-":
            if s[i + 1].isnumeric():
                start = i + 1
                end = i + 1
                while end < n - 1 and s[end + 1].isnumeric():
                    end += 1
                integer = float(s[start: end + 1])
                stack.append(-integer)
                i = end + 1
            else:
                stack.append(character)
        elif character != " ":
            start = i
            end = i
            while end < n - 1 and s[end + 1].isnumeric():
                end += 1
            integer = float(s[start: end + 1])
            stack.append(integer)
            i = end + 1
        i += 1

    # do division and multiplication in stack
    i = 0
    n = len(stack)
    while i < len(stack):
        character = stack[i]
        if (type(character) != int and type(character) != float) and character in "*/":
            if character == "*":
                value = stack[i - 1] * stack[i + 1]
                stack[i - 1] = value
                stack.pop(i + 1)
                stack.pop(i)
                continue
            value = stack[i - 1] / stack[i + 1]
            stack[i - 1] = value
            stack.pop(i + 1)
            stack.pop(i)
            continue
        i += 1

    # do addition and subtraction in stack
    i = 0
    n = len(stack)
    while i < len(stack):
        character = stack[i]
        if (type(character) != int and type(character) != float) and character in "+-":
            if character == "+":
                value = stack[i - 1] + stack[i + 1]
                stack[i - 1] = value
                stack.pop(i + 1)
                stack.pop(i)
                continue
            # for subtraction
            value = stack[i - 1] - stack[i + 1]
            stack[i - 1] = value
            stack.pop(i + 1)
            stack.pop(i)
            continue
        i += 1

    return stack.pop()


print(calculator("20 - 10") == 10)
print(calculator("20 + 10 / 2 * 5 - -5") == 50)

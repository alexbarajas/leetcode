
def decodeString(s: str) -> str:
    # 1. set up a stack
    stack = []
    # 2. go thru the string from left to right, adding to the stack when necessary
    for i in range(len(s)):
        # 2.1. as long as you don't get a closing bracket, append to the stack
        if s[i] != "]":
            stack.append(s[i])
        # 2.2. if you do get a closing bracket, start maneuvering thru the stack
        else:  # for when you do get a closing bracket
            added = ""  # what will be multiplied k times
            while stack[-1] != "[":
                added = stack.pop() + added
            stack.pop()
            k = ""  # times to be multiplied
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(added * int(k))

    # 3. return the stack joined by an empty string
    return "".join(stack)


s = "3[a]2[bc]"
print(decodeString(s))
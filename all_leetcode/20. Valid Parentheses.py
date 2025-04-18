
def isValid(s: str) -> bool:
    # 1. set up a check hashmap that maps the left:right of the parentheses sets
    pairs = {"}": "{", "]": "[", ")": "("}

    # 2. set up an empty stack array, and go thru each character in s
    stack = []
    for character in s:
        # 2.1. if character is not in pairs, append it to the stack
        if character not in pairs:
            stack.append(character)
        # 2.2. if character is in pairs...
        else:
            # 2.2.1. pop the top value from the stack if a stack exists and the top of the stack == pairs[character]
            if stack and stack[-1] == pairs[character]:
                stack.pop()
            # 2.2.2. return False if a stack doesn't exist
            else:
                return False

    # 3. at the end return if there is not a stack
    return not stack

def isValid1(s: str) -> bool:
    brackets = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    stack = []

    for character in s:
        if stack and stack[-1] in brackets and character == brackets[stack[-1]]:
            stack.pop()
        else:
            stack.append(character)

    return not stack



print(isValid("()[]{}"))
print(isValid1("()[]{}"))
print(not isValid("([)]"))
print(not isValid1("([)]"))


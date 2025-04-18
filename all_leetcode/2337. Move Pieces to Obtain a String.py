def canChange(start: str, target: str) -> bool:
    pointer1 = 0
    pointer2 = 0
    n = len(start)
    m = len(target)

    while pointer1 < n and pointer2 < m:
        # move the pointers until they're at a character that isn't "_"
        while pointer1 < n and start[pointer1] == "_":
            pointer1 += 1
        while pointer2 < m and target[pointer2] == "_":
            pointer2 += 1

        # if one pointer reaches the end and the other doesn't, return False
        if pointer1 == n or pointer2 == m:
            return pointer1 == n and pointer2 == m

        # check if the characters at pointer1 and pointer2 are different, if they are return False
        if start[pointer1] != target[pointer2]:
            return False

        # check to see if the move is valid, so if the character is L, pointer1 < pointer2, and if the character is R, pointer1 > pointer2
        if (start[pointer1] == "L" and pointer1 < pointer2) or (start[pointer1] == "R" and pointer1 > pointer2):
            return False

        # shift both pointers
        pointer1 += 1
        pointer2 += 1

    # make sure all the remaining characters are underscores
    while pointer1 < n:
        if start[pointer1] != "_":
            return False
        pointer1 += 1
    while pointer2 < m:
        if target[pointer2] != "_":
            return False
        pointer2 += 1

    # return True at the end
    return True

print(canChange(start = "_L__R__R_", target = "L______RR"))
print(not canChange(start = "R_L_", target = "__LR"))
print(not canChange(start = "_R", target = "R_"))

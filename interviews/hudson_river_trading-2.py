# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# word machine

class WordMachine:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def dup(self):
        if self.size > 0:
            self.stack.append(self.stack[-1])
            self.size += 1
        else:
            return

    def pop(self):
        if self.size > 0:
            self.stack.pop()
            self.size -= 1
        else:
            return

    def add(self):
        if self.size >= 2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.push(a + b)
            self.size -= 2
        else:
            self.size = -1
            return -1

    def subtract(self):
        if self.size >= 2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.push(a - b)
            self.size -= 1
        else:
            self.size = -1
            return -1

    def top(self):
        return self.stack[-1]


def solution(S):
    # write your code in Python 3.6
    wm = WordMachine()
    for step in S.split():
        if step.isdigit():
            wm.push(int(step))
        elif step == "POP":
            wm.pop()
        elif step == "DUP":
            wm.dup()
        elif step == "+":
            wm.add()
        elif step == "-":
            wm.subtract()
    if wm.size <= 0:
        return -1
    else:
        return wm.top()


# array = "1 2 3 4 5"
# print(solution(array))
#
# array = "4 5 6 - 7 +"
# print(solution(array))

array = "5 6 + -"
print(solution(array))

array = "1048575 DUP +" # this is supposed to return -1
print(solution(array))

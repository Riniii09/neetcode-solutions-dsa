import sys

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [sys.maxsize]

    def push(self, val: int) -> None:
        # print("PUSHHH")
        # print(self.minimum)
        result = self.stack.append(val)
        if val < self.minimum[-1]:
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[-1])
        # print(self.minimum)
        return result

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        # print("POPPP")
        # print(self.minimum)
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]

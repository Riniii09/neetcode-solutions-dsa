import sys

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [sys.maxsize]

    def push(self, val: int) -> None:
        print(self.minimum)
        result = self.stack.append(val)
        if val < self.minimum[-1]:
            if val in self.stack:
                self.minimum.append(val)
            else:
                pass
            print(self.minimum[-1])
        return result

    def pop(self) -> None:
        last = self.stack[-1]
        self.stack.pop()
        if self.minimum[-1] == last and last not in self.stack:
            self.minimum.pop()
        else:
            pass
        return 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]

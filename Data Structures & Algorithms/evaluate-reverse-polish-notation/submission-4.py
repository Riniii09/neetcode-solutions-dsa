class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+", "-", "/", "*"]:
                print(i)
                stack.append(i)
            else:
                if stack:
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    print("numbers!!!")
                    print(num1, num2)
                    if i == '+':
                        result = num1 + num2
                    elif i == '-':
                        result = num1 - num2
                    elif i == '*':
                        result = num2 * num1
                    else:
                        result = int(num1 / num2)
                    stack.append(result)
            print(stack)
        return int(stack.pop())
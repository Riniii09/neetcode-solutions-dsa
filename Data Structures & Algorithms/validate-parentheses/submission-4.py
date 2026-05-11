class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        i = 0
        while i < len(s):
            # if stack == []:
            #     print(s[i])
            #     stack.append(s[i])
            #     print(stack)
            if s[i] == ']' and len(stack) > 0 and stack[-1] == '[':
                print(s[i])
                print(stack[-1])
                stack.pop() if len(stack) > 0 else stack.append(s[i])
                print(stack)
            elif s[i] == '}' and len(stack) > 0 and stack[-1] == '{':
                print(s[i])
                print(stack[-1])
                stack.pop() if len(stack) > 0 else stack.append(s[i])
                print(stack)
            elif s[i] == ')' and len(stack) > 0 and stack[-1] == '(':
                print(s[i])
                print(stack[-1])
                stack.pop() if len(stack) > 0 else stack.append(s[i])
                print(stack)
            else:
                print(s[i])
                stack.append(s[i])
                print(stack)
            i = i + 1
            print(i)
        print(len(stack))
        if len(stack) == 0:
            return True
        else:
            return False
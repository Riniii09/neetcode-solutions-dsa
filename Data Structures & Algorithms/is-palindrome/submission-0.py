class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        print(s)
        n = len(s)
        start = 0
        end = n - 1
        for i in range(n // 2):
            print(start)
            print(end)
            print(s[start])
            print(s[end])
            if s[start] != s[end]:
                return False
            start = start + 1
            end = end - 1
        return True
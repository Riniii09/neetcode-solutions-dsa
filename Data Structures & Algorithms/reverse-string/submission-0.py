class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            temp = s[i]
            print("temp " + temp)
            s[i] = s[n-1-i]
            print("first " + s[i])
            s[n-1-i] = temp
            print("last " + s[n-1-i])
        
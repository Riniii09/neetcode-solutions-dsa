class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mins = []
        for i in range(n):
            sub = ""
            j = i + 1
            sub = sub + s[i]
            for j in range(i + 1, n):
                if s[j] in sub:
                    mins.append(j - i)
                    sub = ""
                    break
                mins.append(j - i + 1)
                sub = sub + s[j]
        print(mins)
        if len(s):
            return max(mins) if mins else 1
        else:
            return 0

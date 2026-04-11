class Solution:
    def scoreOfString(self, s: str) -> int:
        # num = []
        # for si in s:
        #     print(ord(si))
        #     num.append(ord(si))
        # print(num)
        # n = len(num)
        # score = 0
        # for i in range(0, n):
        #     if i+1 < n:
        #         score = abs(num[i] - num[i+1]) + score
        #         print(score)
        # return score
        return sum(abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1))
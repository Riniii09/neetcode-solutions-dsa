class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # length = 0
        # s = s.strip()
        # for i in range(0, len(s)):
        #     if s[i] == " ":
        #         length = 0
        #     else:
        #         length = length + 1
        # return length
        spaces = len(s) - 1
        while spaces >= 0 and s[spaces] == ' ':
            spaces -= 1
        
        length = 0
        while spaces >= 0 and s[spaces] != ' ':
            length += 1
            spaces -= 1
        
        return length
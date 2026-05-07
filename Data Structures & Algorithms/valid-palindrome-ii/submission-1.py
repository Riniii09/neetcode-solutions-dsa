class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                shift_start = s[start + 1: end + 1]
                shift_end = s[start: end]
                return shift_start == shift_start[::-1] or shift_end == shift_end[::-1]
            start = start + 1
            end = end - 1
        
        return True
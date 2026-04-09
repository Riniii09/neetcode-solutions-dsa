class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        last_presence = 0
        for i in s:
            try:
                present = t.index(i, last_presence)
                last_presence = present + 1
            except ValueError:
                return False
        return True
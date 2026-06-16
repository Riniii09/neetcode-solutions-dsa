from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_count = Counter(s1)
        results = [0] * window
        start = 0
        while (start + (window - 1)) < len(s2):
            check = s2[start:start + window]
            print(check)
            check_count = Counter(check)
            if check_count == s1_count:
                return True
            start = start + 1
        print(results)
        return False
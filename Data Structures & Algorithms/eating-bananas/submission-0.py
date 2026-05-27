class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        k_max = max(piles)
        result = max(piles)
        while k<=k_max:
            mid = (k + k_max) // 2
            sum = 0
            for pile in piles:
                sum = sum + (pile + mid - 1) // mid
            if sum <= h:
                result = mid
                k_max = mid - 1
            else:
                k = mid + 1
        return result            

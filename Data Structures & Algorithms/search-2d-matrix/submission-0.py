class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = (m * n) - 1

        if not matrix:
            return False
        
        while low <= high:
            mid = (low + high) // 2
            row = mid // n
            col = mid % n
            element = matrix[row][col]
            if element == target:
                return True
            elif element < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        
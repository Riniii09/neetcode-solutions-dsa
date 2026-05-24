class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        max_area = 0
        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                if heights[j] < min_height:
                    min_height = heights[j]
                width = j - i + 1
                area = min_height * width
                if max_area < area:
                    max_area = area
        return max_area
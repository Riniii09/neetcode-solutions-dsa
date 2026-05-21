class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let i = 0;
        let j = heights.length - 1;
        let max = 0;
        while (i < j) {
            let width = j - i;
            let height = Math.min(heights[i], heights[j]);
            let area = width * height;
            if (area > max) {
                max = area;
            }
            if (heights[i] <= heights[j]) {
                i++;
            } else {
                j--;
            }
        }
        return max;
    }
}

class Solution {
    public int[] getConcatenation(int[] nums) {
        int numLength = nums.length;
        int ansLength = 2 * numLength;
        int[] ans = new int[ansLength];
        for (int i = 0; i < numLength; i++) {
            ans[i] = nums[i];
        }
        for (int i = 0; i < numLength; i++) {
            ans[i + numLength] = nums[i];
        }
        System.out.println(Arrays.toString(ans));
        return ans;
    }
}
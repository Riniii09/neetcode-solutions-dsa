class Solution {
    public boolean hasDuplicate(int[] nums) {
        int compare = 0;
        int length = nums.length;
        for (int i = 0; i < length; i++) {
            compare = nums[i];
            for (int j = i + 1; j < length; j++) {
                if(compare == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
}
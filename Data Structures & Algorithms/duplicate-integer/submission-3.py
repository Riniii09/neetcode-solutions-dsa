class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # new_list = []
        # for i in nums:
        #     if i in new_list:
        #         return True
        #     else:
        #         new_list.append(i)
        # return False
        # return len(nums) != len(set(nums))
        new_set = set()
        for i in nums:
            if i in new_set:
                return True
            new_set.add(i)
        return False
            
            
        
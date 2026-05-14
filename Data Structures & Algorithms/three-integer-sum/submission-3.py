class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # result = []
        # for i in range(n):
        #     j = i + 1
        #     for j in range(i+1, n):
        #         k = j + 1
        #         for k in range(j+1, n):
        #             if (nums[i] + nums[j] + nums[k]) == 0:
        #                 if sorted([nums[i], nums[j], nums[k]]) not in result:
        #                     result.append(sorted([nums[i], nums[j], nums[k]]))
        nums = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[left] + nums[i] + nums[right]
                if total < 0:
                    left = left + 1
                elif total > 0:
                    right = right - 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right-1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
        return result
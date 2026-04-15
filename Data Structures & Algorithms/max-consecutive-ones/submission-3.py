class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # result = []
        # counter = 0
        # for i in nums:
        #     if i == 1:
        #         # print("found 1")
        #         # print(i)
        #         counter += 1
        #         # print(counter)
        #     else:
        #         # print("found 0")
        #         # print(i)
        #         counter = 0
        #         # print(counter)
        #     result.append(counter)
        #     # print(result)
        # return max(result)
        ones = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
                if counter > ones:
                    ones = counter
            else:
                counter = 0
        return ones
        
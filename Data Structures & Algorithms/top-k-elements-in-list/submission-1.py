class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        nums = sorted(nums)
        for i in nums:
            if elements.get(i):
                value = elements.get(i) + 1
                elements[i] = value
            else:
                elements[i] = 1
        print(elements)
        print(list(elements)[::-1])
        elements = dict(sorted(elements.items(), key = lambda item: item[1]))
        print(elements)
        elements = list(elements)[::-1]
        result = []
        for i in range(k):
            result.append(elements[i])
        print(result)
        return result
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # set1 = set(s)
        # set2 = set(t)
        
        # diff = set1 - set2
        # print(set1, set2)
        # print(diff)
        # if len(diff) == 0: 
        #     return True
        # return False
        # new_list = []
        # for i in s:
        #     new_list.append(i)
        # for i in t:
        #     if i not in new_list:
        #         return False
        #     pass
        # print(new_list)

        # return True
        from collections import Counter

        count_s = dict(Counter(s))
        print(count_s)

        count_t = dict(Counter(t))
        print(count_t)

        if count_t != count_s:
            return False

        return True
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            print(s)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] = count[ord(char) - ord("a")] + 1
                print(count[ord(char) - ord("a")])
            res[tuple(count)].append(s)
        print(res.keys())
        print(res.values())
        return list(res.values())
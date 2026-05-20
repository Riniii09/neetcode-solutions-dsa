class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        s = ""
        for word in strs:
            length = len(word)
            print(length)
            s = s + str(length) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        result = []
        while i < len(s):
            print(s[i])
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            result.append(word) 
            i = j + 1 + length        
        return result

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        k = 0
        merged = ""
        shorter = ""
        if len(word1) < len(word2):
            length = len(word1)
            shorter = word1
        elif len(word2) < len(word1):
            length = len(word2)
            shorter = word2
        else:
            length = len(word1)
        while k < length:
            print("i = " + str(i))
            print("j = " + str(j))
            merged = merged + word1[i] + word2[j]
            print(merged)
            j = j + 1
            i = i + 1
            k = k + 1
        if shorter == word2:
            print(shorter)
            merged = merged + word1[i:]
            print(merged)
            return merged
        if shorter == word1:
            merged = merged + word2[j:]
            return merged
        else:
            return merged

